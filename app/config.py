import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    """
    Configuration class for Flask application settings.
    Loads sensitive information from environment variables for security.
    """
    # Secret key for securing sessions and cookies
    SECRET_KEY = os.getenv('SECRET_KEY')
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///rent.db'   # URI for the SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # Disable modification tracking to save resources
    # Mail server configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    # Email authentication credentials loaded from environment variables
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')