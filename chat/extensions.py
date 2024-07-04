from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_security import SQLAlchemyUserDatastore, Security
from flask_socketio import SocketIO

db = SQLAlchemy()
migrate = Migrate()
admin = Admin(name='Chat Webanwendung', template_mode='bootstrap3')
socketio = SocketIO()
security = Security()