from flask import Flask, request, session
from flask_restplus import Resource, Api, fields
from flask_cors import CORS

import json
import datetime
import bcrypt
from functools import wraps
from dotenv import load_dotenv
import os
import requests

from database import DB
import utils

# =============== app setting part start ===============
# load secret key
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)
# connect to mongoDB
db = DB()
CORS(app)

api = Api(app,
		#   # Default namespace
		#   default="Airbnb API",
		#   default_label="Airbnb API namespace",
		version = "1.0", 
		#  Documentation Title
		title="Airbnb Database",
		#  Documentation Description
		description="Airbnb backend APIs."
)

# set namespaces, remvoe the default namespace before adding new
api.namespaces.clear()
users = api.namespace('users', description='User APIs')
houses = api.namespace('houses', description='House APIs')
# =============== app setting part end ===============


# =============== data model part start ===============
# user data model
user_model = api.model('user', {
	'email': fields.String(
		required = True, 
		description="Email of the user", 
		help="Email cannot be blank."
	),
	'name': fields.String,
	'password': fields.String,
	'phone': fields.String,
	'role': fields.String
})

# house data model
house_model = api.model('house', {
	'title': fields.String,
	'cover': fields.Url,
	'description': fields.String,
	'provider': fields.String,
	# datetime.datetime.now() 获取当前时间
	'date': fields.DateTime,

	'suburb': fields.String,
	'location': fields.String,
	'price': fields.Integer,
	'size': fields.Integer,
	'bedroom_num': fields.Integer,
	'bathroom_num': fields.Integer,
	'carpark_num': fields.Integer,
	'wifi': fields.Boolean,
	'party_allowed': fields.Boolean,
	'pet_allowed': fields.Boolean
})

# user login data model
user_login_model = api.model('user login', {
	'email': fields.String(
		required = True, 
		description="Email of the user", 
		help="Email cannot be blank."
	),
	'password': fields.String,
})
# =============== data model part end ===============

# =============== login authentication  part start ===============
# require user login
def requires_user(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		if not 'user_role' in session:
			api.abort(401, 'User login requried')
	return decorated

# require provider(landlord or agent) login
# provider is a user with more permission (house info manipulation)
def requires_provider(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		if not 'user_role' in session or session['user_role'] != 'provider':
			api.abort(401, 'Provider login requried')
	return decorated

# =============== login authentication  part end ===============

# ============ user API part start ============
@users.route('/register')
class Register(Resource):
	@users.expect(user_model, validate=True)
	@users.doc(desciption="Register a new user account")
	# register a user account
	def post(self):
		user_data = request.json
		if db.find_user_by_email(user_data['email']):
			return "The email already exists.", 404
		user_data['password'] = bcrypt.hashpw(user_data['password'].encode('utf-8'), bcrypt.gensalt())
		user_id = db.add_user(user_data)
		# set session status
		session['user_id'] = user_id
		session['user_email'] = user_data['email']
		session['user_name'] = user_data['name']
		session['user_role'] = user_data['role']
		return "Registered successfully", 200

@users.route('/login')
class Login(Resource):
	# login a user account
	@users.expect(user_login_model, validate=True)
	@users.doc(desciption="Log in an user account")
	def post(self):
		user_login_data = request.json
		login_user = db.find_user_by_email(user_login_data['email'])
		if login_user == None:
			return "The user email does not exist", 404
		# check password
		if bcrypt.hashpw(user_login_data['password'].encode('utf-8'), login_user['password']) == login_user['password']:
			# set session status
			session['user_id'] = login_user['_id']
			session['user_email'] = login_user['email']
			session['user_name'] = login_user['name']
			session['user_role'] = login_user['role']
			return "Log in successfully", 200

@users.route('/logout')
class Login(Resource):
	@users.doc(desciption="Log out an user account")
	@requires_user
	# log out a user account (need user login)
	def get(self):
		# clear session status
		session.clear()
		return "Log out successfully", 200

@users.route('/<string:user_id>')
class User(Resource):
	@users.doc(description="Delete a user by its ID")
	@requires_user
	# delete user account
	def delete(self, user_id):
		delete_user = db.find_user_by_id(user_id)
		if delete_user:
			# user can only delete his/her account
			if session['user_id'] == user_id:
				db.delete_user(user_id)
				msg = {'message': f'User = {user_id} is removed from the database!'}
				return msg, 200
			else:
				return "Unauthorized delete request", 401
		else:
			return f'User with id {user_id} is not in the database!', 404
		

	@users.expect(user_model, validate=True)
	@users.doc(description="Update user info")
	# update user account
	def patch(self, user_id):
		update_info = request.json
		update_user = db.find_user_by_id(user_id)
		if update_user:
			# user can only modify his/her user data
			if session['user_id'] == user_id:
				db.update_user(user_id, update_info)
				msg = {'message': 'The user info is updated!'}
				return msg, 200
			else:
				return "Unauthorized patch request", 401
		else:
			return f'User with id {user_id} is not in the database!', 404
# ============ user API part end ============

# ============ house API part start ============
@houses.route('/')
@houses.response(200, 'OK')
@houses.response(201, 'Created')
@houses.response(404, 'Error')
class Houses(Resource):
	# @requires_user
	@houses.param('suburb', 'suburb for filtering houses')
	@houses.doc(description="Retrieve all houses info")
	# get all houses
	def get(self):
		all_houses = db.find_all_houses()
		suburb = request.args.get('suburb')
		all_houses = utils.filter_houses(all_houses, suburb)
		return all_houses, 200
	
	@requires_provider
	@houses.doc(description="Upload a new house info")
	@houses.expect(house_model, validate=True)
	# upload a house
	def post(self):
		new_house = request.json
		_id = db.add_house(new_house)
		if _id:
			return "The house is uploaded", 201
		else:
			return "Something is wrong, please try again", 404

@houses.route('/random')
@houses.response(200, 'OK')
@houses.response(201, 'Created')
@houses.response(404, 'Error')
class RandomHouses(Resource):
	@houses.doc(description="Retrieve random houses for the home page")
	# get all houses
	def get(self):
		random_houses = db.find_random_houses()
		return random_houses, 200

@houses.route('/<string:house_id>')
class House(Resource):
	@requires_user
	@houses.doc(description="Retrieve a house by its ID")
	# get house info by its ID
	def get(self, house_id):
		found_house = db.find_house_by_id(house_id)
		if found_house:
			return found_house, 200
		else:
			return f'House with id {house_id} is not in the database!', 404
	
	@requires_provider
	@houses.doc(description="Delete a house by its ID")
	# delete a house
	def delete(self, house_id):
		delete_house = db.find_house_by_id(house_id)
		if delete_house:
			house_provider = delete_house['provider']
			# only the provider of this house can delete this house
			if session['user_id'] == house_provider:
				db.delete_house(house_id)
				msg = {'message': f'House = {house_id} is removed from the database!'}
				return msg, 200
			else:
				return "Unauthorized delete request", 401
		else:
			return f'House with id {house_id} is not in the database!', 404

	@requires_provider
	@houses.expect(house_model, validate=True)
	@houses.doc(description="Update house info")
	# update house info
	def patch(self, house_id):
		update_info = request.json
		update_house = db.find_house_by_id(house_id)
		if update_house:
			house_provider = update_house['provider']
			# only the provider of the house can modify the advertisement
			if session['user_id'] == house_provider:
				db.update_house(house_id, update_info)
				msg = {'message': 'The house info is updated!'}
				return msg, 200
			else:
				return "Unauthorized patch request", 401
		else:
			return f'House with id {house_id} is not in the database!', 404
# ============ house API part end ============

# ============ user saved list part start ============
# ============ user saved list part end ============


# ============ comment API part start ============
# ============ comment API part end ============

# run the app
if __name__ == '__main__':
	app.secret_key = SECRET_KEY
	app.run(debug=True)
