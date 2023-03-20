from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

app.app_context().push()

class Unit(db.Model):
    __tablename__ = 'Units'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    template = db.Column(db.Text)

units = [
    Unit(title="Understanding Your Role", template="1.html"),
    Unit(title="Your Personal Development", template="2.html"),
    Unit(title="Duty of Care", template="3.html"),
    Unit(title="Equality and Diversity", template="4.html"),
    Unit(title="Work in a Person-Centred Way", template="5.html"),
    Unit(title="Communication", template="6.html"),
    Unit(title="Privacy and Dignity", template="7.html"),
    Unit(title="Fluids and Nutrition", template="8.html"),
    Unit(title="Awareness of Mental Health, Dementia and Learning Disabilities", template="9.html"),
    Unit(title="Safeguarding Vulnerable Adults", template="10.html"),
    Unit(title="Safeguarding Vulnerable Children", template="11.html"),
    Unit(title="Basic Life Support", template="12.html"),
    Unit(title="Health and Safety", template="13.html"),
    Unit(title="Handling information", template="14.html"),
    Unit(title="Infection Prevention and Control", template="15.html")
]

for i in units:
    db.session.add(i)
    db.session.commit()