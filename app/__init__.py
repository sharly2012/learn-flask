from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from app.main import main as main_blueprint

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app()

    bootstrap.init_app()
    mail.init_app()
    moment.init_app()
    db.init_app()
    app.register_blueprint(main_blueprint)

    return app
