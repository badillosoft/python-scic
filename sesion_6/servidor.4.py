from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hola/<nombre_py>")
def hola(nombre_py):
	return render_template("hola.html", nombre_html=nombre_py)

app.run()