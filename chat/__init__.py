from flask import Flask
from .extensions import db, migrate, admin, socketio, security
from .models import Role, User
from .views import main_blueprint
from .events import socketio_blueprint
from flask_security import SQLAlchemyUserDatastore, Security

def create_app(config_filename='config'):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    socketio.init_app(app)
    security.init_app(app, SQLAlchemyUserDatastore(db, User, Role))
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(socketio_blueprint)
    
    return app