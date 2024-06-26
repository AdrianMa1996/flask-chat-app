from flask import Flask
from flask_admin import Admin
from flask_migrate import Migrate
from flask_security import SQLAlchemyUserDatastore, Security
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)
app.config.from_object('config')

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(app, model_class=Base)

migrate = Migrate(app, db)

admin = Admin(app, name='Chat Webanwendung', template_mode='bootstrap3')

from chat.models import Role, User

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
app.security = Security(app, user_datastore)

from chat.views import *

if __name__ == '__main__':
    app.run(debug=True)
