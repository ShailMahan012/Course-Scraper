from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

app.app_context().push()


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    firstname = db.Column(db.Text, nullable=False)
    lastname = db.Column(db.Text, nullable=True)

    country = db.Column(db.Text)
    company = db.Column(db.Text)
    addr1 = db.Column(db.Text)
    addr2 = db.Column(db.Text)
    city = db.Column(db.Text)
    postcode = db.Column(db.Integer)

    phone = db.Column(db.Text)

    paid = db.Column(db.Boolean, default=True)
    image_file = db.Column(db.Text, nullable=False, default='user.jpg')

    def __str__(self):
        return f'{self.email} : {self.username}'

    def __repr__(self):
        return f'{self.email} : {self.username}'


class Unit(db.Model):
    __tablename__ = 'Unit'
    unit_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)

class Section(db.Model):
    __tablename__ = 'Section'
    section_id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer)
    title = db.Column(db.Text)
    type = db.Column(db.Text)

class Progress(db.Model):
    __tablename__ = 'Progress'
    progress_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    section_id = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=False)
