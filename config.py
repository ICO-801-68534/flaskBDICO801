from os import getenv 
from dotenv import load_dotenv
class Config(object):
    SECRET_KEY="claveSecreta"
    SESSION_COOKIE_SECURE= False


class DevelopmentConfig(Config):
    load_dotenv()
    DEBUG=True
    SQLALCHEMY_DATABASE_URI= f'mysql+pymysql://{getenv("DB_USERNAME")}:{getenv("DB_PASSWORD")}@127.0.0.1/ico801'
    SQLALCHEMY_TRACK_MODIFICATION= False