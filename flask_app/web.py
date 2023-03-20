#!/usr/bin/python3

from flask import Flask, redirect, render_template


app = Flask(__name__)
@app.route('/')
def index():
	return redirect("/lms/care-certificate")


@app.route("/lms/care-certificate")
def care_certificate():
	return render_template("care_certificate/care_certificate.html")


app.run(port=8081, debug=True)

