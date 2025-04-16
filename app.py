from flask import Flask, render_template
app = Flask(__name__)

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


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
