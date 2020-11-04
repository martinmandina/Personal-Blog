import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martinmandina:alicewambui@localhost/blogs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
     #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SENDER_EMAIL = 'mandinasila@gmail.com'

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martinmandina:alicewambui@localhost/minute'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martinmandina:alicewambui@localhost/minute'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test': TestConfig

}


