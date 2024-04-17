from flask import Blueprint

errors = Blueprint('errors', __name__)

@errors.route('/error')
def error_404():
    return render_template('404.html'), 404

@errors.route('/errors')
def error_500():
    return render_template('500.html'), 500

@errors.route('/errorss')
def error_403():
    return render_template('403.html'), 403
