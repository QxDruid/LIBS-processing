from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig

db = SQLAlchemy()

def create_app(config_class=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    if not app.debug:
        pass

    

    from web_app.lines.views import lines
    app.register_blueprint(lines,  url_prefix='/lines')


    return app

