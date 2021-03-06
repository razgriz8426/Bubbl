from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from .models import db, login_manager
from flask_pagedown import PageDown




bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
pagedown = PageDown()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Razgriz8426?mysql@localhost/db1'
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Razgriz8426?mysql@localhost/db1'
    login_manager.init_app(app)
    pagedown.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app

