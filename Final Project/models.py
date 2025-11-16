from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    """
    Reprezintă un Utilizator în sistem.
    """
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256))
    role = db.Column(db.String(50), default='Developer')

    # Relații cu alte modele:
    reported_tickets = db.relationship('Ticket', foreign_keys='Ticket.reporter_id', backref='reporter', lazy=True)
    assigned_tickets = db.relationship('Ticket', foreign_keys='Ticket.assigned_to_id', backref='assignee', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)

    def set_password(self, password):
        """Generează și setează hash-ul parolei."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifică parola trimisă cu hash-ul stocat."""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Returnează un dicționar cu datele utilizatorului (fără hash-ul parolei)."""
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
        }

    # Metode necesare pentru Flask-Login
    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f'<User {self.username}>'


class Ticket(db.Model):
    """
    Reprezintă un Tichet (Bug/Feature) în sistem.
    """
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='New', nullable=False)
    priority = db.Column(db.String(50), default='Medium', nullable=False)
    type = db.Column(db.String(50), default='Bug', nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Chei Externe
    reporter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    assigned_to_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True, index=True)

    # Relație cu Comentariile
    comments = db.relationship('Comment', backref='ticket', lazy=True,
                               cascade="all, delete-orphan")

    def to_dict(self, include_comments=True):
        """Returnează un dicționar cu datele tichetului."""
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'priority': self.priority,
            'type': self.type,
            'created_at': self.created_at.isoformat(),
            'reporter_id': self.reporter_id,
            'reporter_username': self.reporter.username if self.reporter else None,
            'assigned_to_id': self.assigned_to_id,
            'assignee_username': self.assignee.username if self.assignee else None,
        }
        if include_comments and self.comments:
            # Sortăm comentariile după dată
            sorted_comments = sorted(self.comments, key=lambda c: c.created_at)
            data['comments'] = [comment.to_dict() for comment in sorted_comments]
        return data

    def __repr__(self):
        return f'<Ticket {self.id}: {self.title}>'


class Comment(db.Model):
    """
    Reprezintă un Comentariu atașat unui Tichet.
    """
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Chei Externe
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable=False, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)

    def to_dict(self):
        """Returnează un dicționar cu datele comentariului."""
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'ticket_id': self.ticket_id,
            'author_id': self.author_id,
            'author_username': self.author.username if self.author else None,
        }

    def __repr__(self):
        return f'<Comment {self.id} on Ticket {self.ticket_id}>'


def seed_data(app):
    """
    Adaugă date de bază (utilizatori și tichete) dacă baza de date este goală.
    """
    with app.app_context():
        if User.query.count() == 0:
            app.logger.info("Baza de date este goală. Se adaugă date de test (seed data)...")

            # Utilizatori
            user_admin = User(username='Robert_Alexandru', role='Admin')
            user_admin.set_password('admin_password')

            user_reporter = User(username='Ana_Tester', role='Reporter')
            user_reporter.set_password('tester_password')

            user_dev = User(username='Vlad_Dev', role='Developer')
            user_dev.set_password('dev_password')

            db.session.add_all([user_admin, user_reporter, user_dev])
            db.session.commit()

            # Tichete
            ticket1 = Ticket(
                title='Butonul de Login nu funcționează',
                description='La apasarea butonului de Login, se primește o eroare de rețea. Am verificat consola și am primit 404/401 inițial.',
                status='In Progress',
                priority='Highest',
                type='Bug',
                reporter_id=user_reporter.id,
                assigned_to_id=user_admin.id
            )

            ticket2 = Ticket(
                title='Optimizare performanță API /tickets',
                description='Interogarea tuturor tichetelor devine lentă pe măsură ce adăugăm mai mult de 1000 de înregistrări. Este necesară paginare.',
                status='Open',
                priority='High',
                type='Improvement',
                reporter_id=user_admin.id,
                assigned_to_id=user_dev.id
            )

            db.session.add_all([ticket1, ticket2])
            db.session.commit()

            # Comentarii
            comment1 = Comment(
                content='Am început investigarea. Se pare că este o problemă de CORS la nivel de SocketIO/Flask.',
                ticket_id=ticket1.id,
                author_id=user_admin.id
            )

            comment2 = Comment(
                content='Am identificat și rezolvat problema. Se poate testa din nou.',
                ticket_id=ticket1.id,
                author_id=user_dev.id
            )

            db.session.add_all([comment1, comment2])
            db.session.commit()
            app.logger.info("Datele de test au fost adăugate cu succes.")


def init_login_manager(app, login_manager):
    """Inițializează LoginManager-ul și funcția de încărcare a utilizatorului."""
    from models import User

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        """Funcție necesară pentru a reîncărca utilizatorul din ID-ul stocat în sesiune."""
        return db.session.get(User, int(user_id))