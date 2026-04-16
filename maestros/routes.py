from flask import render_template, request, redirect, url_for, flash
from models import db, Maestros
import forms
from sqlalchemy.exc import IntegrityError
from maestros import maestros_bp 

@maestros_bp.route("/maestros")
def maestros():
    lista_maestros = Maestros.query.all()
    return render_template("maestros/maestros.html", maestros=lista_maestros)

@maestros_bp.route('/registrar_maestro', methods=['GET', 'POST'])
def registrar():
    form = forms.MaestroForm()
    if form.validate_on_submit():
        try:
            nuevo = Maestros(
                matricula=form.id.data,
                nombre=form.nombre.data,
                apellidos=form.apellidos.data,
                especialidad=form.especialidad.data,
                email=form.email.data
            )
            db.session.add(nuevo)
            db.session.commit()
            flash("Maestro registrado correctamente.", "success")
            return redirect(url_for('maestros.maestros'))
        except IntegrityError:
            db.session.rollback()
            flash("Error: La matrícula o el correo ya existen.", "danger")
            
    return render_template("maestros/registrar_maestro.html", form=form)

@maestros_bp.route('/modificar/<int:id>', methods=['GET', 'POST'])
def modificar(id):
    maestre = Maestros.query.get_or_404(id)
    form = forms.MaestroForm(obj=maestre)
    
    if request.method == 'POST':
        maestre.nombre = request.form.get('nombre')
        maestre.apellidos = request.form.get('apellidos')
        maestre.especialidad = request.form.get('especialidad')
        maestre.email = request.form.get('email')
        
        try:
            db.session.commit()
            flash("Datos del maestro actualizados.", "success")
            return redirect(url_for('maestros.maestros'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error al actualizar: {e}", "danger")
            
    return render_template("maestros/editar_maestro.html", form=form, maestro=maestre)

@maestros_bp.route('/detalles/<int:id>')
def detalles(id):
    maestre = Maestros.query.get_or_404(id)
    return render_template("maestros/detalles_maestro.html", maestro=maestre)

@maestros_bp.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar(id):
    maestre = Maestros.query.get_or_404(id)
    form = forms.MaestroForm(obj=maestre)
    
    cursos_conflictivos = maestre.cursos 

    if request.method == 'POST':
        if len(cursos_conflictivos) > 0:
            flash(f"Este maestro tiene {len(cursos_conflictivos)} curso(s). Reasigna los cursos a otro maestro o bórralos antes de continuar.", "warning")
            return redirect(url_for('maestros.maestros'))

        try:
            db.session.delete(maestre)
            db.session.commit()
            flash(f"Maestro {maestre.nombre} eliminado permanentemente.", "success")
            return redirect(url_for('maestros.maestros'))
        except IntegrityError:
            db.session.rollback()
            flash("Error de base de datos al intentar eliminar.", "danger")
            return redirect(url_for('maestros.maestros'))
    
    return render_template("maestros/eliminar_maestro.html", maestro=maestre, form=form, cursos=cursos_conflictivos)