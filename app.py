from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def perdon():
    return render_template('perdon.html')

@app.route('/pqteamo')
def teamo():
    return render_template('pqteamo.html')

@app.route('/pqmgustas')
def megustas():
    return render_template('pqmegustas.html')

@app.route('/qmemolesta')
def molesta():
    return render_template('qmemolesta.html')

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
