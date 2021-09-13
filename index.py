from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')
    
@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

@app.route('/db')
def db():
    return render_template('db.html')

@app.route('/items')
def items():
    return render_template('items.html')

if __name__=='__main__':
    app.run(debug=True)