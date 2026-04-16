from flask import render_template, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from models import db, Alumnos
import forms
from alumnos import alumnos_bp

@alumnos_bp.route("/alumnos", methods=["GET", "POST"])
def vista_alumnos(): 
    create_form = forms.UserForm(request.form)
    lista_alumnos = Alumnos.query.all()
    return render_template("alumnos/alumnos.html", form=create_form, alumno=lista_alumnos)

@alumnos_bp.route("/insertar_alumno", methods=["GET", "POST"])
def insertar_alumno():
    create_form = forms.UserForm(request.form)
    
    if request.method == "POST":
        try:
            alum = Alumnos(
                id=create_form.id.data,
                nombre=create_form.nombre.data,
                amaterno=create_form.amaterno.data,
                apaterno=create_form.apaterno.data,
                edad=create_form.edad.data,
                correo=create_form.correo.data,
            )
            db.session.add(alum)
            db.session.commit()
            return redirect(url_for("alumnos.vista_alumnos"))
            
        except IntegrityError:
            db.session.rollback()
            flash("Esta matrícula ya existe, cámbiala", "error")
            
    return render_template("alumnos/insertar_alumno.html", form=create_form)

@alumnos_bp.route("/detalles_alumno", methods=["GET", "POST"])
def detalles():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        nombre = alum1.nombre
        apaterno = alum1.apaterno
        amaterno = alum1.amaterno
        edad = alum1.edad
        correo = alum1.correo

    return render_template(
        "alumnos/detalles.html",
        id=id,
        nombre=nombre,
        apaterno=apaterno,
        amaterno=amaterno,
        edad=edad,
        correo=correo,
    )

@alumnos_bp.route("/modificar_alumno", methods=["GET", "POST"])
def modificar():
    create_form = forms.UserForm(request.form)
    
    if request.method == "GET":
        id = request.args.get("id")
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get("id")
        create_form.nombre.data = alum1.nombre
        create_form.apaterno.data = alum1.apaterno
        create_form.amaterno.data = alum1.amaterno
        create_form.edad.data = alum1.edad
        create_form.correo.data = alum1.correo

    if request.method == "POST":
        id = request.args.get("id")
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        
        try:
            alum1.id = create_form.id.data
            alum1.nombre = create_form.nombre.data
            alum1.apaterno = create_form.apaterno.data
            alum1.amaterno = create_form.amaterno.data
            alum1.edad = create_form.edad.data
            alum1.correo = create_form.correo.data
            
            db.session.add(alum1)
            db.session.commit()
            return redirect(url_for("alumnos.vista_alumnos"))
            
        except IntegrityError:
            db.session.rollback()
            flash("Esa matrícula ya está en uso por otro alumno, elige otra.", "error")
    
    return render_template("alumnos/modificar.html", form=create_form)

@alumnos_bp.route("/eliminar_alumno", methods=["GET", "POST"])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get("id")
        create_form.nombre.data = alum1.nombre
        create_form.apaterno.data = alum1.apaterno
        create_form.amaterno.data = alum1.amaterno
        create_form.edad.data = alum1.edad
        create_form.correo.data = alum1.correo
        
    if request.method == "POST":
        id = request.form.get("id")
        alum = Alumnos.query.get_or_404(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for("alumnos.vista_alumnos"))
    
    return render_template("alumnos/eliminar.html", form=create_form)

@alumnos_bp.route("/cursos_alumno", methods=["GET"])
def cursos_alumno():
    id = request.args.get("id")
    alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
    return render_template("alumnos/cursos_inscritos.html", alumno=alumno)