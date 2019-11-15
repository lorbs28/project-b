from flask import current_app, Blueprint

api = Blueprint('api', __name__)

@api.route('/health')
def health():
    return 'OKAY!'

@api.route('/env')
def env():
    return current_app.config['ENV']