from flask import Blueprint

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/hello/<name>')
def hello_world(name='World'):
    return f'Hello {name}!'