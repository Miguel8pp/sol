from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from flask import Flask, send_from_directory
from flask import Flask, request, send_file
app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/')
def perdon():
    return send_from_directory('templates', 'perdon.html')

@app.route('/pqteamo')
def teamo():
    return send_from_directory('templates', 'pqteamo.html')

@app.route('/pqmgustas')
def megustas():
    return send_from_directory('templates', 'pqmegustas.html')

@app.route('/qmemolesta')
def molesta():
    return send_from_directory('templates', 'qmemolesta.html')




# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)