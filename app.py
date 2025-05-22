from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from itsdangerous import URLSafeTimedSerializer
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus
import requests
import datetime
from bson import Decimal128
from decimal import Decimal
from bson import ObjectId
from flask import Flask, send_from_directory
from flask import Flask, request, send_file
import subprocess
import yt_dlp
from urllib.parse import urlparse, parse_qs
import traceback
import uuid
import tempfile
import shutil
from urllib.parse import unquote_plus
import re
from werkzeug.utils import secure_filename
from bson import ObjectId
import gridfs
from io import BytesIO
from flask_socketio import SocketIO
from urllib.parse import quote_plus


load_dotenv()

app = Flask(__name__)
bcrypt = Bcrypt(app)  # asegúrate de que 'app' es tu instancia de Flask
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'advpjsh')
socketio = SocketIO(app)  # Inicial iza Flask-SocketIO

# Conexión a MongoDB Atlas
username = os.getenv('MONGO_USERNAME')
password = os.getenv('MONGO_PASSWORD')
username = quote_plus(username)
password = quote_plus(password)
client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.hx8un.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['db1']
collection = db['usuarios']
cancioness = db['canciones'] 

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/teamo')
def teamo():
    return render_template('teamo.html')

@app.route('/pqteamo')
def pqteamo():
    return render_template('pqteamo.html')

@app.route('/pqmgustas')
def pqmegustas():
    return render_template('pqmegustas.html')

@app.route('/qmemolesta')
def qmolesta():
    return render_template('qmemolesta.html')

@app.route('/canciones')
def canciones():
    canciones_lista = cancioness.find() 
    return render_template('canciones.html', cancioness=canciones_lista)

@app.route('/tiempo')
def tiempo():
    return render_template('tiempo.html')

@app.route('/rompe')
def cabezas():
    return render_template('rompecabezas.html')

@app.route("/admin")
def admin_post():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    return render_template("admin.html", cancioness=cancioness.find())  # Renderiza la plantilla con los posts

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usuario_form = request.form.get("usuario") # Renombré a usuario_form para mayor claridad
        contraseña = request.form.get("contraseña")

        datos_user = collection.find_one({'usuario': usuario_form}) # Usa usuario_form aquí
        if datos_user and bcrypt.check_password_hash(datos_user['contrasena'], contraseña):
            session['usuario'] = usuario_form # Guarda la cadena de texto original en la sesión
            if datos_user.get('rol') == 'admin':
                return redirect(url_for('admin_post'))
            else:
                # Si tienes un rol de usuario normal, podrías redirigir a otra página
                # o mostrar un mensaje de éxito. Aquí, por simplicidad, redirigimos a inicio.
                return redirect(url_for('inicio')) # O a donde corresponda para usuarios normales
        else:
            flash("Usuario o contraseña incorrectos. Intenta de nuevo.", "error")

    return render_template('login.html')

@app.route("/admin/nuevo", methods=["POST"])
def nuevo():
    try:
        cancioness.insert_one({
            "titulo": request.form["titulo"],
            "autor": request.form["autor"],
            "cancion": request.form["cancion"],
            "naudio": request.form["naudio"]
        })
        flash("post_created", "Cancion agregada con exito ")  # Clase 'post_created' para mensajes de éxito de creación
    except:
        flash("Error al crear la nueva cancion", "error")  # Clase 'error' para mensajes de error

    return redirect("/admin")


@app.route("/admin/editar/<id>", methods=["POST"])
def editar(id):
    try: 
        cancioness.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "titulo": request.form["titulo"],
            "autor": request.form["autor"],
            "cancion": request.form["cancion"],
            "naudio": request.form["naudio"]
        }}
    )
        flash("post_created", "Cambios realizados con exito")
    except: 
        flash("post_deleted", "Error")
    
    return redirect("/admin")

@app.route("/admin/eliminar/<id>", methods=["POST"])
def eliminar(id):
    try:
        cancioness.delete_one({"_id": ObjectId(id)})
        flash("post_deleted", "Artículo eliminado con éxito")  # Clase 'post_deleted' para mensajes de éxito de eliminación
    except:
        flash("Error al eliminar el artículo", "error")  # Clase 'error' para mensajes de error

    return redirect("/admin")

# Ejecutar la aplicación con SocketIO
if __name__ == '__main__':
    socketio.run(app, debug=True)