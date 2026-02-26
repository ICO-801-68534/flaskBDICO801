# Genera la conexion a la bd

import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = 'claveSecreta'
    SESSSION_COKIE_SECURE = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABABASE_URI = 'mysql=pymysql://admin:root@localhost/ico801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = Config