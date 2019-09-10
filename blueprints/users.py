from flask import Blueprint, request
from factories import UserFactory
users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('/all')
def users_all():
    return "GET all users"


@users_bp.route('/create', methods=['POST'])
def users_create():
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        name = request.json.get('name')
        u = UserFactory.create_user(name, username, password)
        return u.serialize()
    return "method not implemented", 405
