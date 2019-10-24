from flask import Flask, request, session
from flask_restplus import Resource, Api, fields
from flask_cors import CORS

import json
import datetime

# import bcrypt
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

api = Api(
    app,
    #   # Default namespace
    #   default="Airbnb API",
    #   default_label="Airbnb API namespace",
    version="1.0",
    #  Documentation Title
    title="Airbnb Database",
    #  Documentation Description
    description="Airbnb backend APIs.",
)

# set namespaces, remvoe the default namespace before adding new
api.namespaces.clear()
users = api.namespace("users", description="User APIs")
houses = api.namespace("houses", description="House APIs")
savelists = api.namespace("savelists", description="Save List APIs")
comments = api.namespace("comments", description="Comments APIs")
# =============== app setting part end ===============


# =============== data model part start ===============
# user data model
user_model = api.model(
    "user",
    {
        "email": fields.String(
            # required=True,
            description="Email of the user",
            help="Email cannot be blank.",
        ),
        "name": fields.String,
        "profile": fields.Raw,
        "password": fields.String,
        "phone": fields.String,
        "role": fields.String,
    },
)

# house data model
house_model = api.model(
    "house",
    {
        "title": fields.String,
        "cover": fields.String,
        # "cover": fields.Raw,
        "images": fields.List(fields.String),
        # "images": fields.List(fields.Raw),
        "description": fields.String,
        "provider": fields.String,
        # datetime.datetime.now() 获取当前时间
        # "date": fields.DateTime,
        "suburb": fields.String,
        "location": fields.String,
        "price": fields.String,
        "size": fields.String,
        "tenant_num": fields.String,
        "has_wifi": fields.String,
        "party_allowed": fields.String,
        "pet_allowed": fields.String,
        "smoke_allowed": fields.String,
        "lat": fields.String,
        "lng": fields.String,
        "rating_num": fields.String,
        "rating": fields.String,
    },
)

# user login data model
user_login_model = api.model(
    "user login",
    {
        "email": fields.String(
            required=True,
            description="Email of the user",
            help="Email cannot be blank.",
        ),
        "password": fields.String,
    },
)
# =============== data model part end ===============

# =============== login authentication  part start ===============
# require user login
# def requires_user(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         if not "user_role" in session:
#             api.abort(401, "User login requried")

#     return decorated


# # require provider(landlord or agent) login
# # provider is a user with more permission (house info manipulation)
# def requires_provider(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         if not "user_role" in session or session["user_role"] != "provider":
#             api.abort(401, "Provider login requried")

#     return decorated


# =============== login authentication  part end ===============

# ============ user API part start ============
@api.response(200, "OK")
@api.response(201, "Created")
@api.response(404, "Error")
@users.route("/")
class Users(Resource):
    @api.expect(user_model, validate=True)
    @api.doc(description="Register a new user account")
    # register a user account
    def post(self):
        user_data = request.json
        if db.find_user_by_email(user_data["email"]):
            return "The email already exists.", 404

        # store the encrypted user password
        # user_data["password"] = bcrypt.hashpw(
        #     user_data["password"].encode("utf-8"), bcrypt.gensalt()
        # )
        user_id = db.add_user(user_data)
        # set session status
        # session["user_id"] = user_id
        # session["user_email"] = user_data["email"]
        # session["user_name"] = user_data["name"]
        # session["user_role"] = user_data["role"]

        # store active user info
        active_users[user_id] = user_data
        # return user id
        return user_id + " " + user_data["role"], 200

    @api.doc(description="get all users (only used for test)")
    def get(self):
        users = db.find_all_users()
        return users, 200


@users.route("/login")
class Login(Resource):
    # login a user account
    @api.expect(user_login_model, validate=True)
    @api.doc(description="Log in an user account")
    def post(self):
        user_login_data = request.json
        login_user = db.find_user_by_email(user_login_data["email"])
        if utils.check_logged_in(active_users, user_login_data["email"]):
            print(user_login_data["email"] + " has Already logged in")
            return login_user["_id"] + " " + login_user["role"], 200
        if login_user == None:
            return "The user email does not exist", 404

        # check encrypted password
        # if bcrypt.hashpw(user_password.encode("utf-8"), user_password) == user_password:
        if user_login_data["password"] == login_user["password"]:
            # set session status
            # session["user_id"] = login_user["_id"]
            # session["user_email"] = login_user["email"]
            # session["user_name"] = login_user["name"]
            # session["user_role"] = login_user["role"]

            # store active user info
            active_users[login_user["_id"]] = login_user
            # return user id
            return login_user["_id"] + " " + login_user["role"], 200
        else:
            return "Unauthorized login request", 401


@users.route("/logout/<string:user_id>")
class Logout(Resource):
    @api.doc(description="Log out an user account")
    # @requires_user
    # log out a user account (need user login)
    def get(self, user_id):
        # clear session status
        # if session["user_id"] == user_id:
        #     session.clear()
        #     return "Log out successfully", 200

        if user_id in active_users:
            del active_users[user_id]
        print("User is not in the active list, maybe the server has restarted.")
        return "Log out successfully", 200


@users.route("/<string:user_id>")
class User(Resource):
    @api.doc(description="Return user info (except password)")
    def get(self, user_id):
        userData = db.find_user_by_id(user_id)
        if userData:
            del userData["password"]
            return userData, 200
        else:
            return f"User with id {user_id} is not in the database!", 404

    @api.doc(description="Delete a user by its ID")
    # @requires_user
    # delete user account
    def delete(self, user_id):
        delete_user = db.find_user_by_id(user_id)
        if delete_user:
            # user can only delete his/her account
            # if session["user_id"] == user_id:
            #     db.delete_user(user_id)
            #     msg = {"message": f"User = {user_id} is removed from the database!"}
            #     return msg, 200

            if user_id == delete_user["_id"]:
                db.delete_user(user_id)
                if user_id in active_users:
                    del active_users[user_id]
                msg = {"message": f"User = {user_id} is removed from the database!"}
                return msg, 200
            else:
                return "Unauthorized delete request", 401
        else:
            return f"User with id {user_id} is not in the database!", 404

    # @api.expect(user_model, validate=True)
    @api.doc(description="Update user info")
    # update user account
    def patch(self, user_id):
        update_info = request.json
        print(update_info)
        # remove empty property in update info
        update_info = utils.get_valid_update_info(update_info)

        update_user = db.find_user_by_id(user_id)
        if update_user:
            # user can only modify his/her user data
            # if session["user_id"] == user_id:
            #     db.update_user(user_id, update_info)
            #     msg = {"message": "The user info is updated!"}
            #     return msg, 200

            db.update_user(user_id, update_info)
            msg = {"message": "The user info is updated!"}
            return msg, 200
        else:
            return f"User with id {user_id} is not in the database!", 404


# ============ user API part end ============

# ============ house API part start ============
@houses.route("/")
class Houses(Resource):
    @api.param("keyword", "keyword for filtering houses")
    @api.param("suburb", "suburb for filtering houses")
    @api.param("min_price", "minimum price for filtering houses")
    @api.param("max_price", "maximum price for filtering houses")
    @api.param("start_date", "start date for filtering houses")
    @api.param("end_date", "end date for filtering houses")
    @api.param("size", "house size for filtering houses")
    @api.param("tenant_num", "tenant number for filtering houses")
    @api.param("pet_allowed", "pet allowed for filtering houses")
    @api.param("smoke_allowed", "smoke allowed for filtering houses")
    @api.param("has_wifi", "has wifie for filtering houses")
    @api.doc(description="Retrieve all houses info")
    # get all houses
    def get(self):
        keyword = request.args.get("keyword")
        suburb = request.args.get("suburb")
        min_price = (
            int(request.args.get("minPrice")) if request.args.get("minPrice") else None
        )
        max_price = (
            int(request.args.get("maxPrice")) if request.args.get("maxPrice") else None
        )
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")

        all_houses = db.find_all_houses()
        all_houses = utils.filter_houses(
            houses=all_houses,
            keyword=keyword,
            suburb=suburb,
            min_price=min_price,
            max_price=max_price,
            start_date=start_date,
            end_date=end_date,
        )
        return all_houses, 200

    # @requires_provider
    @api.doc(description="Upload a new house")
    @api.expect(house_model, validate=False)
    # upload a house
    def post(self):
        new_house = request.json
        _id = db.add_house(new_house)
        if _id:
            return f"House with id {_id} is uploaded", 201
        else:
            return "Something is wrong, please try again", 404


@houses.route("/random")
class RandomHouses(Resource):
    @api.doc(description="Retrieve random houses for the home page")
    # get all houses
    def get(self):
        random_houses = db.find_random_houses()
        return random_houses, 200


@houses.route("/<string:house_id>")
class House(Resource):
    @api.doc(description="Retrieve a house by its ID")
    # get house info by its ID
    def get(self, house_id):
        found_house = db.find_house_by_id(house_id)
        if found_house:
            return found_house, 200
        else:
            return f"House with id {house_id} is not in the database!", 404


@houses.route("/<string:provider_id>/<string:house_id>")
class HouseOfProvider(Resource):
    # @requires_provider
    @api.doc(description="Delete a house by its ID")
    # delete a house
    def delete(self, provider_id, house_id):
        delete_house = db.find_house_by_id(house_id)
        if delete_house:
            house_provider = delete_house["provider"]
            # only the provider of this house can delete this house
            if provider_id == house_provider:
                db.delete_house(house_id)
                msg = {"message": f"House = {house_id} is removed from the database!"}
                return msg, 200
            else:
                return "Unauthorized delete request", 401
        else:
            return f"House with id {house_id} is not in the database!", 404

    # @requires_provider
    # @api.expect(house_model, validate=True)
    @api.doc(description="Update house info")
    # update house info
    def patch(self, provider_id, house_id):
        update_info = request.json

        # remove empty update properties
        update_info = utils.get_valid_update_info(update_info)

        update_house = db.find_house_by_id(house_id)
        if update_house:
            house_provider = update_house["provider"]
            # only the provider of the house can modify the advertisement
            if provider_id == house_provider:
                db.update_house(house_id, update_info)
                msg = {"message": "The house info is updated!"}
                return msg, 200
            else:
                return "Unauthorized patch request", 401
        else:
            return f"House with id {house_id} is not in the database!", 404


@houses.route("/providedby/<string:provider_id>")
class HousesOfProvider(Resource):
    @api.param("keyword", "keyword for filtering houses")
    @api.param("suburb", "suburb for filtering houses")
    @api.param("min_price", "minimum price for filtering houses")
    @api.param("max_price", "maximum price for filtering houses")
    @api.param("start_date", "start date for filtering houses")
    @api.param("end_date", "end date for filtering houses")
    @api.param("size", "house size for filtering houses")
    @api.param("tenant_num", "tenant number for filtering houses")
    @api.param("pet_allowed", "pet allowed for filtering houses")
    @api.param("smoke_allowed", "smoke allowed for filtering houses")
    @api.param("has_wifi", "has wifie for filtering houses")
    @api.doc(description="Get the provider's house list")
    def get(self, provider_id):
        keyword = request.args.get("keyword")
        suburb = request.args.get("suburb")
        min_price = (
            int(request.args.get("minPrice")) if request.args.get("minPrice") else None
        )
        max_price = (
            int(request.args.get("maxPrice")) if request.args.get("maxPrice") else None
        )
        print(min_price, max_price)
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")

        houses_of_provider = db.find_user_houses(provider_id)
        houses_of_provider = utils.filter_houses(
            houses=houses_of_provider,
            keyword=keyword,
            suburb=suburb,
            min_price=min_price,
            max_price=max_price,
            start_date=start_date,
            end_date=end_date,
        )
        return houses_of_provider, 200

@houses.route("/savelist/<string:user_id>")
class HousesOfUserSavelist(Resource):
    @api.doc(description="Get houses in the user's savelist")
    def get(self, user_id):
        user_savelist = db.find_savelist_of_user(user_id)
        user_savelist_houses = db.find_savelist_houses(user_savelist)
        return user_savelist_houses, 200
# ============ house API part end ============

# ============ user saved list part start ============
@savelists.route("/")
class Savelists(Resource):
    @api.doc(description="Get all savelist")
    def get(self):
        return db.find_all_savelists(), 200

@savelists.route("/<string:user_id>")
class SavelistOfUser(Resource):
    @api.doc(description="Get the user's savelist")
    def get(self, user_id):
        user_savelist = db.find_savelist_of_user(user_id)
        return user_savelist, 200

@savelists.route("/<string:user_id>/add/<string:house_id>")
class AddHouseToSavelist(Resource):
    @api.doc(description="Add house id to user's savelist")
    def get(self, user_id, house_id):
        db.add_to_user_savelist(user_id, house_id)
        return "Added", 201
# ============ user saved list part end ============


# ============ comment API part start ============
@comments.route("/<string:house_id>")
class CommentsOfHouse(Resource):
    @api.doc(description="Get full comments' info of house")
    def get(self, house_id):
        house_comments = db.find_comments_of_house(house_id)["comments"]
        return house_comments, 200

@comments.route("/<string:house_id>/add/<string:user_id>/content/<string:comment>")
class AddCommentToHouse(Resource):
    @api.doc(description="Add comment to house")
    def get(self, house_id, user_id, comment):
        db.add_comment_to_house(house_id, user_id, comment)
        return "Added", 201
# ============ comment API part end ============

# run the app
if __name__ == "__main__":
    app.secret_key = SECRET_KEY
    # store active users
    active_users = {}
    app.run(debug=True)

