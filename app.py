from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return (
        '<h1>¡Hola desde mi aplicación!</h1>'
        '<p>Esta es una app Flask muy básica.</p>'
    )


@app.route('/saludo/<nombre>')
def saludo_personalizado(nombre):
    return (
        f'<h2>¡Hola, {nombre}!</h2>'
        '<p>Bienvenido a la aplicación Flask.</p>'
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
