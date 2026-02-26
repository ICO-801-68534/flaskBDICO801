from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig

from models import db, Alumnos
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)
db.init_app(app)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/usuarios")
def usuarios():
	return render_template("usuarios.html")

if __name__ == '__main__':
	app.run(debug=True)
