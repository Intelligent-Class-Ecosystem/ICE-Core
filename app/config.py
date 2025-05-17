class Config:
    SECRET_KEY = 'dev'
    FLASK_ENV = 'development'
    FLASK_DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ice-core.db'