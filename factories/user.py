from models import User


class UserFactory(object):
    @classmethod
    def create_user(cls, name, username, password):
        u = User(name=name, username=username, password=password)
        u.save()
        return u

    @classmethod
    def get_all_users(cls):
        return User.all()
