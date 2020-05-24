from flask import Flask, render_template
from .config import configs
from .models import db, User


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    

    @app.route('/')
    def index():
        return 'hello shiyanlou'

    return app
