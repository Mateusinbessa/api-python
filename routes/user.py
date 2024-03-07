from flask import Blueprint

from controllers.user import login

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/login', methods=['POST'])
def loginRoute():
    return login()