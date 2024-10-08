from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.login'  # Redirigir a login si no está autenticado
login_manager.login_message_category = 'info'  # Opcional: mostrar un mensaje si no está autenticado

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    from app.routes import main
    app.register_blueprint(main)
    
    return app
