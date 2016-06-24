import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('Razgriz8426?secretkey') or 'Razgriz8426?secretkey'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
#    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
#    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
#    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass
   
    
class DevelopmentConfig(Config):
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'Razgriz8426?secretkey'
#    MAIL_SERVER = 'smtp.googlemail.com'
#    MAIL_PORT = 587
#    MAIL_USE_TLS = True
#    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
#    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
#    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
#        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Razgriz8426?mysql@localhost/db1'
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'Razgriz8426?secretkey'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Razgriz8426?mysql@localhost/db1'
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'Razgriz8426?secretkey'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': TestingConfig
}

