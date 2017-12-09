# Práctica X - Servicios Web (Flask)

Un *Servicio Web* consiste en un programa que se ejecuta en un servidor que provee recursos a diversos clientes conectados en la misma red o en internet. Estos sirven para darle al cliente una capa intermedia entre los recursos del sistema operativo y las bases de datos de una forma más sencilla. Por ejemplo, existen diversos servicios web para enviar la hora, realizar operaciones complejas, mostrar los resultados de una búsqueda en la base de datos, entre otros.

En Python una de las formas más simples para proveer servicios web es usar la librería llamada *Flask* la cual instancia un servidor web de forma rápida. Flask utiliza el protocolo *http* y provee los recursos mediante los métodos `GET` y `POST` al recibir una ruta.

> Documentación: http://flask.pocoo.org/ | http://jinja.pocoo.org/docs/2.10/

## Montar un servidor en Flask

Recuerda instalar Flask con `pip install flask`. El ejemplo de abajo muestra como montar un servidor en flask que provee la ruta `/hola`. Al montar el servidor, este podrá ser accedido en el puerto por defecto `5000` en el host `localhost`.

~~~py
from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def hola():
	return "Hola mundo"

app.run()
~~~

Si abrimos un navegador en la ruta `http://localhost:5000/hola` podremos acceder al recurso que envia nuestro servidor, en este caso un texto que dice `Hola mundo`.

## Rutas dinámicas

Podemos establecer rutas dinámicas para poder proveer recursos más precisos y únicos, por ejemplo, si quisieramos recibir el nombre de la persona en la misma ruta y responder con un mensaje personalizado, haríamos:

~~~py
from flask import Flask

app = Flask(__name__)

@app.route("/hola/<nombre>")
def hola(nombre):
	return "Hola {}".format(nombre)

app.run()
~~~

Si abrimos un navegador en la ruta `http://localhost:5000/hola/pepe` nos devolverá el texto `Hola pepe`, si accedemos a la ruta `http://localhost:5000/hola/ana` nos devolverá el texto `Hola ana`.

## Plantillas HTML

Flask utiliza un sistema de plantillas HTML basado en `Jinja2`, el cual permite renderizar archivos HTML. Lo primero que debemos hacer es crear una carpeta llamada `templates` y dentro de esta colocar los archivos html. Por ejemplo, si quisieramos montar un servidor que en la ruta `/` muestre el archivo `index.html`, deberíamos colocar el archivo `index.html` en la carpeta `templates` y luego hacer:

~~~py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

app.run()
~~~

Adicionalmente podemos pasar parámetros a nuestros archivos html desde la función `render_template`:

~~~py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hola/<nombre_py>")
def hola(nombre_py):
	return render_template("hola.html",
		nombre_html=nombre_py)

app.run()
~~~

El ejemplo anterior le enviaría la variable `nombre_html` a la plantilla con el valor extraído de la ruta dinámica `nombre_py`. Para recibir y mostrar dicha variable en nuestro archivo html usaríamos Jinja para ello:

~~~html
<h1>Hola {{ nombre_html }}</h1>
~~~ 

## Procesar un formulario con el método *POST*

Para controlar un formulario *POST* debemos recuperar los campos del formulario, supongamos que tenemos el siguiente html que establece un formulario que se procesa en la ruta `/login`:

> HTML `templates/login.html`

~~~html
<form action="/login" method="POST">
    <label for="usuario">Usuario:</label><br>
    <input name="usuario" type="text"><br>
    <label for="clave">Contraseña:</label><br>
    <input name="clave" type="password"><br>
    <input type="submit" value="ingresar">
</form>
~~~

> PYTHON

~~~py
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def login():
	return render_template("login.html")

@app.route("/login", methods=["POST"])
def foo():
	usuario = request.form["usuario"]
	clave = request.form["clave"]
	# TODO: Validar usuario y clave
	print "Ingresando con %s (%s)" % (usuario, clave)
	return redirect("/")

app.run()
~~~

## Problemas

* Crear un formulario que reciba los datos de una persona

* Procesar los datos del formulario con flask y guardarlos en un diccionario

* Guardar el diccionario con los datos de la persona en mongo

* Proveer una ruta llamada `/personas` que devuelva un arreglo de diccionarios con los datos de todas las personas

<br><br>
<hr>
<small>
Python Científico - Alan Badillo Salas (badillo.soft@hotmail.com)<br>
Instituto Politécnico Nacional - Centro de Investigación en Cómputo
</small>
