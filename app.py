import os
from flask import Flask
from config import *
from blueprints import auth_bp, users_bp

app = Flask(__name__)

try:
    if os.environ['ENV'] == 'development':
        app.config.from_object(DevConfig)
    elif os.environ['ENV'] == 'staging':
        app.config.from_object(StagingConfig)
    else:
        app.config.from_object(ProductionConfig)
except KeyError as exc:
    app.config.from_object(ProductionConfig)

app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)


@app.route('/')
def home():
    return "Home"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
