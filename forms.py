from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, EmailField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class UserForm(Form):
    id = IntegerField("ID")
    nombre = StringField("Nombre")
    apaterno = StringField("APaterno")
    amaterno = StringField("AMaterno")
    edad = IntegerField("Edad")
    correo = EmailField("Correo")

class MaestroForm(FlaskForm):
    id = IntegerField("Matricula")
    nombre = StringField("Nombre")
    apellidos = StringField("Apellidos")
    especialidad = StringField("Especialidad")
    email = EmailField("Email")


class CursoForm(FlaskForm):
    id = IntegerField("ID")
    nombre = StringField("Nombre del Curso", validators=[DataRequired()])
    descripcion = TextAreaField("Descripción")
    maestro_id = SelectField("Maestro Asignado", coerce=int, validators=[DataRequired()])

class InscripcionForm(FlaskForm):
    alumno_id = SelectField("Seleccionar Alumno", coerce=int, validators=[DataRequired()])
    curso_id = SelectField("Seleccionar Curso", coerce=int, validators=[DataRequired()])