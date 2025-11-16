import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request
from flask_socketio import SocketIO, join_room
from flask_cors import CORS
from dotenv import load_dotenv
from flask_login import LoginManager

# Importă db (instanța SQLAlchemy), funcția seed_data, și init_login_manager
from models import db, seed_data, init_login_manager
from routes import main, api_bp

# Încărcare variabile de mediu (.env)
load_dotenv()


# --- setup_logging ---
def setup_logging(app):
    """Configurarea logger-ului pentru a scrie în fișier și consolă."""
    log_level = logging.DEBUG
    app.logger.setLevel(log_level)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    # Handler pentru fișier (obligatoriu UTF-8)
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10, encoding='utf-8')
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)

    # Adaugă handler-ul de fișier doar dacă nu există deja
    if not any(isinstance(handler, RotatingFileHandler) for handler in app.logger.handlers):
        app.logger.addHandler(file_handler)

    if not app.logger.handlers:
        logging.basicConfig(level=log_level)


# --- Crearea și configurarea aplicației Flask ---
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('MYSQL_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inițializare componente
setup_logging(app)
socketio = SocketIO(app, cors_allowed_origins="*", manage_session=False, async_mode='threading')
CORS(app, supports_credentials=True)

# Inițializare LoginManager
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "api_bp.login"
init_login_manager(app, login_manager)

# Inițializare SQLAlchemy și registre Blueprint-uri
db.init_app(app)
app.register_blueprint(main)
app.register_blueprint(api_bp, url_prefix='/api')


@socketio.on('connect')
def handle_connect():
    """
    Gestionarea conexiunilor noi SocketIO.
    """
    join_room('global')
    app.logger.debug(f"Client conectat: {request.sid}. Adăugat la camera 'global'.")


@socketio.on('disconnect')
def handle_disconnect():
    app.logger.debug(f"Client deconectat: {request.sid}")




# RULARE ȘI INIȚIALIZARE BAZĂ DE DATE

if __name__ == '__main__':
    with app.app_context():
        app.logger.info("Se încearcă crearea tabelelor în baza de date MySQL...")
        try:
            # db.create_all() va crea tabelele cu noua structură
            # Datorită 'cascade', tabelele vor fi create cu Foreign Keys corecte.
            db.create_all()
            app.logger.info("Tabelele bazei de date create/verificate cu succes.")

            # Adaugă date de test dacă baza de date este goală
            seed_data(app)

        except Exception as e:
            app.logger.error(
                f"EROARE CRITICĂ la conexiunea MySQL: Asigurați-vă că serverul MySQL rulează și URL-ul din .env este corect: {e}")
            # Dacă baza de date nu este disponibilă, serverul nu ar trebui să pornească.
            exit(1)  # Ieșire cu cod de eroare

    app.logger.info("Serverul Flask pornește...")
    socketio.run(app, debug=True, port=int(os.getenv("PORT", 5000)))