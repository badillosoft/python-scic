from flask import Flask

app = Flask(__name__)

@app.route("/hola/<nombre>")
def hola(nombre):
	return "Hola {}".format(nombre)

app.run()