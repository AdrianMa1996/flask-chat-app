from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .extensions import db
from .models import Message
from .dtos import convert_message_to_messagedto

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route("/", methods=['GET', 'POST'])
@login_required
def start_page():
    if request.method == 'POST':
        current_user_id = current_user.id

        new_message = Message(
            sender_id=current_user_id,
            content=request.form['content']
        )

        db.session.add(new_message)
        db.session.commit()
        
    messages_from_db = Message.query.order_by(Message.created_at).all()
    messages_dtos = [convert_message_to_messagedto(message) for message in messages_from_db]
    return render_template('index.html', messages=messages_dtos)