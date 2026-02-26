from flask_sqlalchemy import SQLAlchemy
import datetime


db: SQLAlchemy = SQLAlchemy()

class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido_paterno = db.Column(db.String(150), nullable=False)
    apellido_materno = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)