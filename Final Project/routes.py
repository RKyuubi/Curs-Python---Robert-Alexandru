from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
import logging
from models import db, User, Ticket, Comment
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from flask_login import login_user, logout_user, current_user, login_required

main = Blueprint('main', __name__)
api_bp = Blueprint('api_bp', __name__)

app_logger = logging.getLogger('werkzeug')

# Funcția care va fi folosită pentru emitere
def global_emit(event, data, room='global'):
    try:
        from app import socketio
        socketio.emit(event, data, room=room)
    except ImportError as e:
        app_logger.error(f"Eroare la importul socketio în ruta. Poate fi un import circular: {e}")
    except Exception as e:
        app_logger.error(f"Eroare la emiterea SocketIO: {e}")


@main.route('/')
def index():
    """
    Ruta principală care redă fișierul index.html din directorul 'templates'.
    """
    return render_template('index.html')


@main.route('/status', methods=['GET'])
def status():
    """Returnează starea serverului."""
    return jsonify({'status': 'running', 'async_mode': 'threading'})


@api_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return jsonify({"error": "Autentificare necesară. Trimiteți datele (username/password) prin POST."}), 401

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    remember = data.get('remember', False)

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        # Autentificare de succes
        login_user(user, remember=remember)
        app_logger.info(f"Utilizatorul '{username}' s-a logat cu succes.")
        return jsonify({
            "message": "Autentificare reușită",
            "user": user.to_dict()
        }), 200
    else:
        # Autentificare eșuată
        app_logger.warning(f"Tentativă eșuată de login pentru utilizatorul '{username}'.")
        return jsonify({"error": "Nume de utilizator sau parolă incorectă"}), 401


@api_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    current_username = current_user.username
    logout_user()
    app_logger.info(f"Utilizatorul '{current_username}' s-a deconectat.")
    return jsonify({"message": "Deconectare reușită"}), 200


@api_bp.route('/user_info', methods=['GET'])
def get_user_info():
    if current_user.is_authenticated:
        return jsonify({
            "is_authenticated": True,
            "user": current_user.to_dict()
        }), 200
    else:
        return jsonify({
            "is_authenticated": False,
            "user": None
        }), 200


@api_bp.route('/tickets', methods=['GET', 'POST'])
@login_required
def manage_tickets():
    if request.method == 'GET':
        try:
            # Preluăm toate tichetele și le includem comentariile pentru a le afișa pe client
            tickets = Ticket.query.all()
            return jsonify([t.to_dict(include_comments=True) for t in tickets]), 200
        except Exception as e:
            app_logger.error(f"Eroare la preluarea tuturor biletelor: {e}")
            return jsonify({"error": "Eroare la interogarea bazei de date"}), 500

    elif request.method == 'POST':
        data = request.get_json()

        assigned_to_username = data.get('assigned_to_username')
        assigned_to_user = None
        if assigned_to_username:
            assigned_to_user = User.query.filter_by(username=assigned_to_username).first()
            if not assigned_to_user:
                return jsonify({"error": f"Utilizatorul '{assigned_to_username}' (Assignee) nu există."}), 404

        if not data.get('title') or not data.get('description'):
            return jsonify({"error": "Lipsesc câmpurile obligatorii (titlu, descriere)."}), 400

        try:
            new_ticket = Ticket(
                title=data['title'],
                description=data['description'],
                status=data.get('status', 'Open'),
                priority=data.get('priority', 'Medium'),
                type=data.get('type', 'Bug'),
                reporter_id=current_user.id,
                assigned_to_id=assigned_to_user.id if assigned_to_user else None
            )

            db.session.add(new_ticket)
            db.session.commit()

            global_emit('new_ticket', new_ticket.to_dict(include_comments=True), room='global')

            return jsonify(new_ticket.to_dict(include_comments=True)), 201
        except Exception as e:
            app_logger.error(f"Eroare la crearea tichetului: {e}")
            db.session.rollback()
            return jsonify({"error": "Eroare internă a serverului la creare"}), 500


@api_bp.route('/tickets/<int:ticket_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
@login_required
def manage_single_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        return jsonify({"error": f"Tichetul cu ID-ul {ticket_id} nu a fost găsit."}), 404

    if request.method == 'GET':
        return jsonify(ticket.to_dict(include_comments=True)), 200

    elif request.method in ['PUT', 'PATCH']:
        data = request.get_json()

        # Dacă se încearcă modificarea Assigned To, căutăm user-ul după nume
        if 'assigned_to_username' in data:
            assigned_to_username = data['assigned_to_username']
            if assigned_to_username:
                assigned_to_user = User.query.filter_by(username=assigned_to_username).first()
                if not assigned_to_user:
                    return jsonify({"error": f"Utilizatorul '{assigned_to_username}' (Assignee) nu există."}), 404
                data['assigned_to_id'] = assigned_to_user.id
            else:
                data['assigned_to_id'] = None

            del data['assigned_to_username']

        for key, value in data.items():
            if hasattr(ticket, key) and key not in ['id', 'created_at', 'reporter_id']:
                setattr(ticket, key, value)

        ticket.updated_at = datetime.utcnow()

        try:
            db.session.commit()
            global_emit('ticket_updated', ticket.to_dict(include_comments=True), room='global')
            return jsonify(ticket.to_dict(include_comments=True)), 200
        except Exception as e:
            app_logger.error(f"Eroare la actualizarea tichetului {ticket_id}: {e}")
            db.session.rollback()
            return jsonify({"error": "Eroare internă a serverului la actualizare"}), 500

    elif request.method == 'DELETE':
        # DELETE
        try:
            ticket_id_deleted = ticket.id  # Stocăm ID-ul înainte de ștergere
            db.session.delete(ticket)
            db.session.commit()
            global_emit('ticket_deleted', {'id': ticket_id_deleted}, room='global')
            return jsonify({"message": f"Tichetul cu ID-ul {ticket_id_deleted} a fost șters cu succes."}), 200
        except Exception as e:
            app_logger.error(f"Eroare la ștergerea tichetului {ticket_id}: {e}")
            db.session.rollback()
            return jsonify({"error": "Eroare internă a serverului la ștergere"}), 500


@api_bp.route('/comments', methods=['POST'])
@login_required
def add_comment():
    data = request.get_json()
    content = data.get('content')
    ticket_id_str = data.get('ticket_id')

    author_id = current_user.id

    if not content or not ticket_id_str:
        return jsonify({"error": "Lipsesc câmpurile obligatorii (content, ticket_id)."}), 400

    new_comment = None

    try:
        try:
            ticket_id = int(ticket_id_str)
        except ValueError:
            return jsonify({"error": f"ID-ul tichetului '{ticket_id_str}' este invalid."}), 400

        ticket = db.session.get(Ticket, ticket_id)
        if not ticket:
            return jsonify({"error": "Biletul specificat nu există."}), 404

        # Creare Comentariu
        new_comment = Comment(
            content=content,
            ticket_id=ticket.id,
            author_id=author_id
        )

        db.session.add(new_comment)
        db.session.commit()

        db.session.refresh(new_comment)

    except Exception as e:
        app_logger.error("Eroare CRITICĂ la COMMIT/REFRESH-ul comentariului. Traceback:", exc_info=True)
        db.session.rollback()
        return jsonify({"error": "Eroare internă la baza de date (Commit/Refresh)."}), 500

    try:
        if new_comment:
            comment_data = {
                'id': int(new_comment.id),
                'content': str(new_comment.content),
                'created_at': new_comment.created_at.isoformat(),
                'ticket_id': int(new_comment.ticket_id),
                'author_id': int(new_comment.author_id),
                'author_username': str(current_user.username)
            }

            global_emit('new_comment', comment_data, room='global')

            # Răspuns de succes
            return jsonify(comment_data), 201

    except Exception as e:
        app_logger.error("Eroare CRITICĂ la SERIALIZARE/SOCKETIO (Eroare de tipare sau SocketIO). Traceback:",
                         exc_info=True)
        return jsonify({"error": "Eroare la serializarea datelor sau SocketIO."}), 500


@api_bp.route('/users', methods=['GET', 'POST'])
@login_required
def manage_users():
    if request.method == 'GET':
        users = User.query.all()
        return jsonify([u.to_dict() for u in users]), 200

    elif request.method == 'POST':
        if current_user.role != 'Admin':
            return jsonify({"error": "Doar administratorii pot crea utilizatori noi."}), 403

        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        role = data.get('role', 'Developer')

        if not username or not password:
            return jsonify({"error": "Numele de utilizator și parola sunt obligatorii"}), 400

        try:
            new_user = User(username=username, role=role)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return jsonify(new_user.to_dict()), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({"error": f"Utilizatorul '{username}' există deja."}), 409
        except Exception as e:
            app_logger.error(f"Eroare la adăugarea utilizatorului: {e}")
            return jsonify({"error": "Eroare internă a serverului"}), 500