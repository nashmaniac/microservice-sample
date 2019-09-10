from orator import Model
import time
import math
from werkzeug.security import generate_password_hash


class UserObserver(object):
    def creating(user):
        if not hasattr(user, 'id'):
            user.id = str(int(time.time()*math.pow(10, 9)))
        user.password = generate_password_hash(user.password)
        print(user)



class User(Model):
    __fillable__ = ['username', 'name', 'password']
    __hidden__ = ['password']
    __guarded__ = ['created_at', 'updated_at']


User.observe(UserObserver)
