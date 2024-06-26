from flask import redirect, render_template, request, send_from_directory
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from chat import app, db
from .models import Message

@app.route("/", methods=['GET', 'POST'])
@login_required
def start_page():
    if request.method == 'POST':
        new_message = Message(
            user = "nameOfUser",
            content = request.form['content']
        )

        db.session.add(new_message)
        db.session.commit()
    messages_from_db = Message.query.order_by(Message.created_at).all()
    return render_template('index.html', messages=messages_from_db, name="nameOfUser")
