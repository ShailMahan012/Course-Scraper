#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Shail"

app.run(port=8081, debug=True)

