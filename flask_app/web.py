#!/usr/bin/python3

from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
app.app_context().push()

class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    firstname = db.Column(db.Text, nullable=False)
    lastname = db.Column(db.Text, nullable=True)

    country = db.Column(db.Text)
    company = db.Column(db.Text)
    street = db.Column(db.Text)
    addr2 = db.Column(db.Text)
    town = db.Column(db.Text)
    postcode = db.Column(db.Integer)

    phone = db.Column(db.Text)

    paid = db.Column(db.Boolean, default=True)
    image_file = db.Column(db.Text, nullable=False, default='user.jpg')

    def __str__(self):
        return f'{self.email} : {self.username}'

    def __repr__(self):
        return f'{self.email} : {self.username}'


class Units(db.Model):
    __tablename__ = 'Units'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    template = db.Column(db.Text)


class Unit_Sections(db.Model):
    __tablename__ = 'Unit_sections'
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer)
    title = db.Column(db.Text)
    template = db.Column(db.Text)

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        print(dict(request.form))
        input()
    return render_template("login.html")
    


@app.route('/')
def index():
    return redirect("/lms/care-certificate")


@app.route("/lms/care-certificate")
def care_certificate():
    return render_template("care_certificate/care_certificate.html")


@app.route("/lms/care-certificate/unit/<int:unit_id>")
def unit(unit_id):
    return render_template("care_certificate/index.html")


@app.route("/lms/care-certificate/unit/<int:unit_id>/topic/<int:topic_id>")
def topic(unit_id, topic_id):
    return render_template("care_certificate/topic/6.html")


if __name__ == "__main__":
    app.run(port=8081, debug=True)

