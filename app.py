from flask import Flask
from routes.libros import libros
from db import db

app = Flask(__name__)
app.register_blueprint(libros)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@150.136.131.180:33060/Biblioteca"

db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)