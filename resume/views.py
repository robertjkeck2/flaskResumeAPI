import json
from collections import OrderedDict

from flask import request, jsonify, abort
from flask.views import MethodView

from models import Contact, Education, Career, Projects, Skills, db, app


class ContactView(MethodView):

	def get(self):
		contact = Contact.query.first()
		if not contact:
			error = {
				'error': 'No contact info.  Please use POST to create new contact info.'
			}
			return jsonify(error)
		res = OrderedDict()
		res['name'] = contact.name
		res['email'] = contact.email
		res['phone_number'] = contact.phone_number
		res['website'] = contact.website
		return jsonify(res)

	def post(self):
		if len(Contact.query.all()) == 0:
			name = request.form.get('name')
			email = request.form.get('email')
			phone_number = request.form.get('phone_number')
			website = request.form.get('website')
			contact = Contact(name, email, phone_number, website)
			db.session.add(contact)
			db.session.commit()
			return jsonify({contact.id: {
				'name': contact.name,
				'email': contact.email,
				'phone_number': contact.phone_number,
				'website': contact.phone_number
			}})
		else:
			error = {
				'error': 'Adding new contact info is not allowed.  Please use GET to view contact info.'
			}
			return jsonify(error)

class EducationView(MethodView):

	def get(self, id=None, page=1):
		if not id:
			education = Education.query.all()
			if not education:
				error = {
					'error': 'No education info.  Please use POST to create new education info.'
				}
				return jsonify(error)
			res = OrderedDict()
			educations = []
			for edu in education:
				res['university'] = edu.university
				res['date_range'] = edu.date_range
				res['degree'] = edu.degree
				res['gpa'] = edu.gpa
				res['detail'] = edu.detail
				educations.append(OrderedDict(res))
			return jsonify(educations)
		else:
			education = Education.query.filter_by(id=id).first()
			if not education:
				error = {
					'error': 'No education info.  Please use POST to create new education info.'
				}
				return jsonify(error)
			res = OrderedDict()
			res['university'] = education.university
			res['date_range'] = education.date_range
			res['degree'] = education.degree
			res['gpa'] = education.gpa
			res['detail'] = education.detail
		return jsonify(res)

	def post(self):
		if len(Education.query.all()) < 2:
			university = request.form.get('university')
			date_range = request.form.get('date_range')
			degree = request.form.get('degree')
			gpa = request.form.get('gpa')
			detail = request.form.get('detail')
			education = Education(university, date_range, degree, gpa, detail)
			db.session.add(education)
			db.session.commit()
			return jsonify({education.id: {
				'university': education.university,
				'date_range': education.date_range,
				'degree': education.degree,
				'gpa': education.gpa,
				'detail': education.detail
			}})
		else:
			error = {
				'error': 'Adding new education info is not allowed.  Please use GET to view education info.'
			}
			return jsonify(error)

class CareerView(MethodView):

	def get(self, id=None, page=1):
		if not id:
			career = Career.query.all()
			if not career:
				error = {
					'error': 'No career info.  Please use POST to create new career info.'
				}
				return jsonify(error)
			careers = []
			res = OrderedDict()
			for car in career:
				res['employer'] = car.employer
				res['date_range'] = car.date_range
				res['location'] = car.location
				res['position'] = car.position
				res['detail'] = car.detail
				careers.append(OrderedDict(res))
			return jsonify(careers)
		else:
			career = Career.query.filter_by(id=id).first()
			if not career:
				error = {
					'error': 'No career info.  Please use POST to create new career info.'
				}
				return jsonify(error)
			res = OrderedDict()
			res['employer'] = career.employer
			res['date_range'] = career.date_range
			res['location'] = career.location
			res['position'] = career.position
			res['detail'] = career.detail
		return jsonify(res)

	def post(self):
		if len(Career.query.all()) < 3:
			employer = request.form.get('employer')
			date_range = request.form.get('date_range')
			location = request.form.get('location')
			position = request.form.get('position')
			detail = request.form.get('detail')
			career = Career(employer, date_range, location, position, detail)
			db.session.add(career)
			db.session.commit()
			return jsonify({career.id: {
				'employer': career.employer,
				'date_range': career.date_range,
				'location': career.location,
				'position': career.position,
				'detail': career.detail
			}})
		else:
			error = {
				'error': 'Adding new career info is not allowed.  Please use GET to view career info.'
			}
			return jsonify(error)

class ProjectsView(MethodView):

	def get(self, id=None, page=1):
		if not id:
			project = Projects.query.all()
			if not project:
				error = {
					'error': 'No project info.  Please use POST to create new project info.'
				}
				return jsonify(error)
			projects = []
			res = OrderedDict()
			for proj in project:
				res['name'] = proj.name
				res['url'] = proj.url
				res['detail'] = proj.detail
				projects.append(OrderedDict(res))
			return jsonify(projects)
		else:
			project = Projects.query.filter_by(id=id).first()
			if not project:
				error = {
					'error': 'No project info.  Please use POST to create new project info.'
				}
				return jsonify(error)
			res = OrderedDict()
			res['name'] = project.name
			res['url'] = project.url
			res['detail'] = project.detail
		return jsonify(res)

	def post(self):
		if len(Projects.query.all()) < 3:
			name = request.form.get('name')
			url = request.form.get('url')
			detail = request.form.get('detail')
			project= Projects(name, url, detail)
			db.session.add(project)
			db.session.commit()
			return jsonify({project.id: {
				'name': project.name,
				'url': project.url,
				'detail': project.detail
			}})
		else:
			error = {
				'error': 'Adding new project info is not allowed.  Please use GET to view project info.'
			}
			return jsonify(error)

class SkillsView(MethodView):

	def get(self, id=None, page=1):
		if not id:
			skill = Skills.query.all()
			if not skill:
				error = {
					'error': 'No skill info.  Please use POST to create new skill info.'
				}
				return jsonify(error)
			skills = []
			res = OrderedDict()
			for ski in skill:
				res['skill'] = ski.skill
				res['category'] = ski.category
				res['experience'] = ski.experience
				skills.append(OrderedDict(res))
			return jsonify(skills)
		else:
			skill = Skills.query.filter_by(id=id).first()
			if not skill:
				error = {
					'error': 'No skill info.  Please use POST to create new skill info.'
				}
				return jsonify(error)
			res = OrderedDict()
			res['skill'] = skill.skill
			res['category'] = skill.category
			res['experience'] = skill.experience
		return jsonify(res)

	def post(self):
		if len(Skills.query.all()) < 3:
			skill = request.form.get('skill')
			category = request.form.get('category')
			experience = request.form.get('experience')
			skill = Skills(skill, category, experience)
			db.session.add(skill)
			db.session.commit()
			return jsonify({skill.id: {
				'skill': skill.skill,
				'category': skill.category,
				'experience': skill.experience
			}})
		else:
			error = {
				'error': 'Adding new skill info is not allowed.  Please use GET to view skill info.'
			}
			return jsonify(error)

contact_view = ContactView.as_view('contact')
app.add_url_rule('/contact/', view_func=contact_view, methods=['GET', 'POST',])

education_view = EducationView.as_view('education')
app.add_url_rule('/education/', view_func=education_view, methods=['GET', 'POST',])
app.add_url_rule('/education/<int:id>', view_func=education_view, methods=['GET',])

career_view = CareerView.as_view('career')
app.add_url_rule('/career/', view_func=career_view, methods=['GET', 'POST',])
app.add_url_rule('/career/<int:id>', view_func=career_view, methods=['GET',])

project_view = ProjectsView.as_view('projects')
app.add_url_rule('/projects/', view_func=project_view, methods=['GET', 'POST',])
app.add_url_rule('/project/<int:id>', view_func=project_view, methods=['GET',])

skill_view = SkillsView.as_view('skills')
app.add_url_rule('/skills/', view_func=skill_view, methods=['GET', 'POST',])
app.add_url_rule('/skill/<int:id>', view_func=skill_view, methods=['GET',])

