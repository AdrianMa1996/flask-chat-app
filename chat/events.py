from flask import Blueprint
from flask_socketio import emit
from .extensions import socketio, db
from .models import Message
from .dtos import convert_message_to_messagedto

socketio_blueprint = Blueprint('socketio', __name__)

@socketio.on("send_message")
def handle_send_message():
    print("New message")
    messages_from_db = Message.query.order_by(Message.created_at).all()
    messages_dtos = [convert_message_to_messagedto(message).to_dict() for message in messages_from_db]
    emit("receive_message", {"messages": messages_dtos}, broadcast=True)