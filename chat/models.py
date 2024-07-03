from flask_admin.contrib.sqla import ModelView
from flask_security.models import fsqla_v3 as fsqla
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func
from datetime import datetime

from chat import admin, db


# Chat

class Message(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    sender_id: Mapped[int]
    chat_room_id: Mapped[int]
    content: Mapped[str]
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)

class ChatRoom(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_one_id: Mapped[int]
    user_two_id: Mapped[int]


# Flask-Security-Too

fsqla.FsModels.set_db_info(db)


class Role(db.Model, fsqla.FsRoleMixin):
    pass


class User(db.Model, fsqla.FsUserMixin):
    pass


admin.add_view(ModelView(Message, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))

