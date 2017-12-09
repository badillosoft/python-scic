from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/llenar/encuesta")
def foo():
	return render_template("encuesta.html")

@app.route("/recibir/encuesta", methods=["POST"])
def bar():
	sexo = request.form["r1"]
	dias = request.form["r2"]

	print(sexo, dias)

	return "Gracias por participar :D"

app.run()