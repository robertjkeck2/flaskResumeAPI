from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////var//www/api.robertjohnkeck.com/db/resume.db'
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)

class Contact(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	email = db.Column(db.String(255))
	phone_number = db.Column(db.String(255))
	website = db.Column(db.String(255))

	def __init__(self, name, email, phone_number, website):
		self.name = name
		self.email = email
		self.phone_number = phone_number
		self.website = website

	def __repr__(self):
		return "<{}'s Contact Info>".format(self.name) 

class Education(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	university = db.Column(db.String(255))
	date_range = db.Column(db.String(255))
	degree = db.Column(db.String(255))
	gpa = db.Column(db.String(255))
	detail = db.Column(db.String(455))

	def __init__(self, university, date_range, degree, gpa, detail):
		self.university = university
		self.date_range = date_range
		self.degree = degree
		self.gpa = gpa
		self.detail = detail

	def __repr__(self):
		return "<Education>" 

class Career(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	employer = db.Column(db.String(255))
	date_range = db.Column(db.String(255))
	location = db.Column(db.String(255))
	position = db.Column(db.String(255))
	detail = db.Column(db.String(455))

	def __init__(self, employer, date_range, location, position, detail):
		self.employer = employer
		self.date_range = date_range
		self.location = location
		self.position = position
		self.detail = detail

	def __repr__(self):
		return "<Careers>"

class Projects(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	url = db.Column(db.String(255))
	detail = db.Column(db.String(255))

	def __init__(self, name, url, detail):
		self.name = name
		self.url = url
		self.detail = detail

	def __repr__(self):
		return "<Projects>"

class Skills(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	skill = db.Column(db.String(255))
	category = db.Column(db.String(255))
	experience = db.Column(db.String(255))

	def __init__(self, skill, category, experience):
		self.skill = skill
		self.category = category
		self.experience = experience

	def __repr__(self):
		return "<Skills>"

db.create_all()
db.session.commit()
