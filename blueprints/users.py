from flask import Blueprint

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('/all')
def users_all():
    return "GET all users"
