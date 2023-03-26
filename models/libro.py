from db import db

class Libro(db.Model):
    __tablename__ = "libros"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(255), nullable=False)
    autor = db.Column(db.String(255), nullable=False)
    genero = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))
    portada = db.Column(db.String(255))

    def __init__(self, titulo, autor, genero, descripcion, portada):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.descripcion = descripcion
        self.portada = portada

    def serialize(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "genero": self.genero,
            "descripcion": self.descripcion,
            "portada": self.portada,
        }