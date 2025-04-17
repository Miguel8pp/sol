from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'advpjsh')
socketio = SocketIO(app)  # Inicializa Flask-SocketIO

# Conexión a MongoDB Atlas
username = os.getenv('MONGO_USERNAME')
password = os.getenv('MONGO_PASSWORD')
username = quote_plus(username)
password = quote_plus(password)
client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.hx8un.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['db1']
messages_collection = db['mensajes_chat'] #define la coleccion de mensajes para el chat.

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
    return render_template('canciones.html')

@app.route('/tiempo')
def tiempo():
    return render_template('tiempo.html')

@app.route('/rompe')
def cabezas():
    return render_template('rompecabezas.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@socketio.on('send_message')
def handle_message(data):
    message = data['message']
    messages_collection.insert_one({'message': message})
    emit('receive_message', {'message': message}, broadcast=True)

# Ejecutar la aplicación con SocketIO
if __name__ == '__main__':
    socketio.run(app, debug=True) #usa socketio.run para ejecutar la app