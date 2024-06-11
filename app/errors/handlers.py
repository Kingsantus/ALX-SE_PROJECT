from flask import Blueprint, render_template

# Create a blueprint named 'errors'
errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error=None):
    """
    Error handler for HTTP 404 - Not Found.
    Renders the 404.html template.
    """
    return render_template('404.html'), 404

@errors.app_errorhandler(405)
def error_405(error=None):
    """
    Error handler for HTTP 405 - Method Not Allowed.
    Renders the 405.html template.
    """
    return render_template('405.html'), 405

@errors.app_errorhandler(500)
def error_500(error=None):
    """
    Error handler for HTTP 500 - Internal Server Error.
    Renders the 500.html template.
    """
    return render_template('500.html'), 500

@errors.app_errorhandler(403)
def error_403(error=None):
    """
    Error handler for HTTP 403 - Forbidden.
    Renders the 403.html template.
    """
    return render_template('403.html'), 403
