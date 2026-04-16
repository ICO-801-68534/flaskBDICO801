from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from config import DevelopmentConfig

from models import db

from maestros import maestros_bp
from alumnos import alumnos_bp 
from cursos import cursos_bp
from inscripciones import ins_bp

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)  
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

app.register_blueprint(maestros_bp)
app.register_blueprint(alumnos_bp) 
app.register_blueprint(cursos_bp)
app.register_blueprint(ins_bp)

@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)