from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from app.config import Config

# Initialize SQLAlchemy for database management
db = SQLAlchemy()
# Initialize Flask-SocketIO for real-time communication
socketio = SocketIO()
# Initialize Bcrypt for password hashing
bcrypt = Bcrypt()
# Initialize Flask-Login for user session management
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
# Initialize Flask-Mail for email handling
mail  = Mail()

def create_app(config_class=Config):
    """
    Create and configure the Flask application.

    Parameters:
    config_class (class): Configuration class for Flask application settings.

    Returns:
    Flask: Configured Flask application instance.
    """
    # Initialize the Flask application
    app = Flask(__name__)
    # Load configuration from the provided config class
    app.config.from_object(Config)
    # Set the folder for templates
    app.template_folder = 'templates'
    # Initialize extensions with the app instance
    db.init_app(app)            # Initialize SQLAlchemy
    bcrypt.init_app(app)        # Initialize Bcrypt for password hashing
    login_manager.init_app(app) # Initialize Flask-Login for user session management
    mail.init_app(app)          # Initialize Flask-Mail for email handling
    socketio.init_app(app)      # Initialize Flask-SocketIO for real-time communication
    # Import and register blueprints for different parts of the application
    from app.chats.routes import messages
    from app.main.routes import main
    from app.posts.routes import posts
    from app.reviews.routes import reviews
    from app.users.routes import users
    from app.errors.handlers import errors

    app.register_blueprint(messages)    # Register chat-related routes
    app.register_blueprint(main)        # Register main application routes
    app.register_blueprint(posts)       # Register post-related routes
    app.register_blueprint(reviews)     # Register review-related routes
    app.register_blueprint(users)       # Register user-related routes
    app.register_blueprint(errors)      # Register error handlers

    return app


from app.socket.routes import handle_message
# Register a Socket.IO event handler for the 'send_message' event
socketio.on_event('send_message', handle_message)