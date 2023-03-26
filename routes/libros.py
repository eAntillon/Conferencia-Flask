from flask import Blueprint, render_template, request, redirect, Response, jsonify
from db import db
from models.libro import Libro

libros = Blueprint("libros", __name__)

@libros.route("/")
def listarLibros():
    libros = Libro.query.all()
    return render_template("index.html", libros=libros)

@libros.route("/getAll", methods=["GET"])
def get():
    libros = Libro.query.all()
    return Response(response=jsonify([libro.serialize() for libro in libros]), status=200)


@libros.route("/add", methods=["POST"])
def crearLibro():
    print(request.form)
    titulo = request.form["titulo"]
    autor = request.form["autor"]
    genero = request.form["genero"]
    descripcion = request.form["descripcion"]
    portada = request.form["portada"]

    nuevoLibro = Libro(titulo, autor, genero, descripcion, portada)
    db.session.add(nuevoLibro)
    db.session.commit()
    return redirect("/")


@libros.route("/update/<id>", methods=["GET", "POST"])
def actualizarLibro(id):
    libro = Libro.query.get(id)
    if request.method == "GET":
        return render_template("update.html", titulo="Actualizar Libro", libro=libro)
    else:
        libro.titulo = request.form["titulo"]
        libro.autor = request.form["autor"]
        libro.genero = request.form["genero"]
        libro.descripcion = request.form["descripcion"]
        libro.portada = request.form["portada"]
        db.session.commit()
        return redirect("/")


@libros.route("/delete/<id>", methods=["POST"])
def eliminarLibro(id):
    print(id)
    libro = Libro.query.get(id)
    db.session.delete(libro)
    db.session.commit()
    return redirect("/")
