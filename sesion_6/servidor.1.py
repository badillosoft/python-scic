from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def hola():
	return "Hola mundo"

app.run()