from flask import Flask, request, session
from flask_restplus import Resource, Api, fields
from flask_cors import CORS

import json
import datetime

from functools import wraps
import requests

from database import DB
import utils

# =============== app setting part start ===============
app = Flask(__name__)
# connect to mongoDB
db = DB()
CORS(app)

# store active users
active_users = {}

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
        "profile": fields.String,
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
        "description": fields.String,
        # cover url and images url list
        "cover": fields.String,
        "images": fields.List(fields.String),
        # provider's id
        "provider": fields.String,
        "suburb": fields.String,
        "location": fields.String,
        "price": fields.String,
        "size": fields.String,
        "tenant_num": fields.String,
        # available facilities: wifi, kitchen, carpark, air conditioning
        "wifi": fields.Boolean,
        "kitchen": fields.Boolean,
        "carpark": fields.Boolean,
        "ac": fields.Boolean,
        # latitude and longitude to display in google map
        "lat": fields.String,
        "lng": fields.String,
        # rating and rating number
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
            return "The email already exists.", 400
        user_id = db.add_user(user_data)
        # store active user info
        active_users[user_id] = user_data
        # return user id, user role and user name
        return user_id + " " + user_data["role"] + " " + user_data["name"], 200

    @api.doc(description="get all users (only used for test)")
    def get(self):
        users = db.find_all_users()
        return users, 200


@users.route("/login")
class Login(Resource):
    @api.expect(user_login_model, validate=True)
    @api.doc(description="Log in an user account")
    def post(self):
        user_login_data = request.json
        login_user = db.find_user_by_email(user_login_data["email"])
        # check if the login email exist or not
        if login_user == None:
            return "The user email does not exist", 400
        # check if the user is in active user list or not
        if utils.check_logged_in(active_users, user_login_data["email"]):
            print(user_login_data["email"] + " has Already logged in")
            return login_user["_id"] + " " + login_user["role"] + " " + login_user["name"], 200
        # if the password is correct, store user in active users and return user's info
        if user_login_data["password"] == login_user["password"]:
            # store active user info
            active_users[login_user["_id"]] = login_user
            # return user id
            return login_user["_id"] + " " + login_user["role"] + " " + login_user["name"], 200
        else:
            return "Email or password is incorrect!", 400


@users.route("/logout/<string:user_id>")
class Logout(Resource):
    @api.doc(description="Log out an user account")
    def get(self, user_id):
        # if the user is in the active list, remove it from the list
        if user_id in active_users:
            del active_users[user_id]
        print("User is not in the active list, maybe the server has restarted.")
        return "Log out successfully", 200


@users.route("/<string:user_id>")
class User(Resource):
    @api.doc(description="Return user info (except password)")
    def get(self, user_id):
        userData = db.find_user_by_id(user_id)
        # check if the user id exist or not
        if userData:
            del userData["password"]
            return userData, 200
        else:
            return f"User with id {user_id} is not in the database!", 400

    @api.doc(description="Delete a user by its ID")
    def delete(self, user_id):
        delete_user = db.find_user_by_id(user_id)
        # check if the user id exist or not
        if delete_user:
            # delete user's house data first to make sure there is no dirty data in database
            db.delete_houses_of_user(user_id)
            # then delete the user account
            db.delete_user(user_id)
            # if the user is in active user list, remove it from the list
            if user_id in active_users:
                del active_users[user_id]
            msg = {"message": f"User = {user_id} is removed from the database!"}
            return msg, 200
        else:
            return f"User with id {user_id} is not in the database!", 400

    # @api.expect(user_model, validate=True)
    @api.doc(description="Update user info")
    def patch(self, user_id):
        update_info = request.json
        # remove empty property in update info
        update_info = utils.get_valid_update_info(update_info)

        update_user = db.find_user_by_id(user_id)
        # check if the user id exist or not
        if update_user:
            db.update_user(user_id, update_info)
            msg = {"message": "The user info is updated!"}
            return msg, 200
        else:
            return f"User with id {user_id} is not in the database!", 400
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
    @api.param("carpark", "has carpark for filtering houses")
    @api.param("ac", "has ac for filtering houses")
    @api.param("kitchen", "has kitchen for filtering houses")
    @api.param("wifi", "has wifie for filtering houses")
    @api.param("tenant_num", "tenant number for filtering houses")
    @api.param("order_type", "ordering method")
    @api.doc(description="Retrieve all houses info")
    def get(self):
        # get search/filter/sort data from the request's query data
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

        wifi = True if request.args.get("wifi") == "true" else False
        ac = True if request.args.get("ac") == "true" else False
        kitchen = True if request.args.get("kitchen") == "true" else False
        carpark = True if request.args.get("carpark") == "true" else False
        
        tenant_num = (
            int(request.args.get("tenant_num")) if request.args.get("tenant_num") else None
        )
        order_type = request.args.get("order_type")

        # find all houses first
        all_houses = db.find_all_houses()
        # filter and sort the result based on the search/filter/sort input
        all_houses = utils.filter_houses(
            houses=all_houses,
            keyword=keyword,
            suburb=suburb,
            min_price=min_price,
            max_price=max_price,
            start_date=start_date,
            end_date=end_date,
            wifi=wifi,
            ac=ac,
            kitchen=kitchen,
            carpark=carpark,
            tenant_num=tenant_num,
            order_type=order_type
        )
        # return the filtered houses
        return all_houses, 200

    @api.doc(description="Upload a new house")
    @api.expect(house_model, validate=False)
    def post(self):
        new_house = request.json
        # set house's rating and rating number to default value
        new_house["rating"] = "0"
        new_house["rating_num"] = "0"
        # change the house's suburb to title format
        new_house["suburb"] = new_house["suburb"].title()
        _id = db.add_house(new_house)
        if _id:
            return f"House with id {_id} is uploaded", 201
        else:
            return "Something is wrong, please try again", 500


@houses.route("/random")
class RandomHouses(Resource):
    @api.doc(description="Retrieve random houses")
    def get(self):
        # get random houses
        random_houses = db.find_random_houses()
        return random_houses, 200


@houses.route("/<string:house_id>")
class House(Resource):
    @api.doc(description="Retrieve a house by its ID")
    def get(self, house_id):
        found_house = db.find_house_by_id(house_id)
        # check if the house id exist or not
        if found_house:
            return found_house, 200
        else:
            return f"House with id {house_id} is not in the database!", 400


@houses.route("/<string:provider_id>/<string:house_id>")
class HouseOfProvider(Resource):
    @api.doc(description="Delete a house by its ID")
    def delete(self, provider_id, house_id):
        delete_house = db.find_house_by_id(house_id)
        # check if the house id exist or not
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
            return f"House with id {house_id} is not in the database!", 400

    @api.doc(description="Update house info")
    def patch(self, provider_id, house_id):
        update_info = request.json
        # remove empty update properties
        update_info = utils.get_valid_update_info(update_info)

        update_house = db.find_house_by_id(house_id)
        # check if the house id exist or not
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
            return f"House with id {house_id} is not in the database!", 400


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
    @api.param("carpark", "has carpark for filtering houses")
    @api.param("ac", "has ac for filtering houses")
    @api.param("kitchen", "has kitchen for filtering houses")
    @api.param("wifi", "has wifie for filtering houses")
    @api.param("tenant_num", "tenant num for filtering houses")
    @api.param("order_type", "ordering method")
    @api.doc(description="Get all provider's houses")
    def get(self, provider_id):
        # get search/filter/sort data from the request's query data
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

        wifi = True if request.args.get("wifi") == "true" else False
        ac = True if request.args.get("ac") == "true" else False
        kitchen = True if request.args.get("kitchen") == "true" else False
        carpark = True if request.args.get("carpark") == "true" else False

        tenant_num = (
            int(request.args.get("tenant_num")) if request.args.get("tenant_num") else None
        )
        order_type = request.args.get("order_type")

        # find all provider's hosues
        houses_of_provider = db.find_user_houses(provider_id)
        # filter and sort the result based on the search/filter/sort input
        houses_of_provider = utils.filter_houses(
            houses=houses_of_provider,
            keyword=keyword,
            suburb=suburb,
            min_price=min_price,
            max_price=max_price,
            start_date=start_date,
            end_date=end_date,
            wifi=wifi,
            ac=ac,
            kitchen=kitchen,
            carpark=carpark,
            tenant_num=tenant_num,
            order_type=order_type,
        )
        return houses_of_provider, 200

@houses.route("/savelist/<string:user_id>")
class HousesOfUserSavelist(Resource):
    @api.param("keyword", "keyword for filtering houses")
    @api.param("suburb", "suburb for filtering houses")
    @api.param("min_price", "minimum price for filtering houses")
    @api.param("max_price", "maximum price for filtering houses")
    @api.param("start_date", "start date for filtering houses")
    @api.param("end_date", "end date for filtering houses")
    @api.param("size", "house size for filtering houses")
    @api.param("tenant_num", "tenant number for filtering houses")
    @api.param("carpark", "has carpark for filtering houses")
    @api.param("ac", "has ac for filtering houses")
    @api.param("kitchen", "has kitchen for filtering houses")
    @api.param("wifi", "has wifie for filtering houses")
    @api.param("tenant_num", "tenant num for filtering houses")
    @api.param("order_type", "ordering method")
    @api.doc(description="Get houses in the user's savelist")
    def get(self, user_id):
        # get search/filter/sort data from the request's query data
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

        wifi = True if request.args.get("wifi") == "true" else False
        ac = True if request.args.get("ac") == "true" else False
        kitchen = True if request.args.get("kitchen") == "true" else False
        carpark = True if request.args.get("carpark") == "true" else False

        tenant_num = (
            int(request.args.get("tenant_num")) if request.args.get("tenant_num") else None
        )
        order_type = request.args.get("order_type")
        
        # get all houses in user's save list
        user_savelist = db.find_savelist_of_user(user_id)
        user_savelist_houses = db.find_savelist_houses(user_savelist)
        # filter and sort the result based on the search/filter/sort input
        user_savelist_houses = utils.filter_houses(
            houses=user_savelist_houses,
            keyword=keyword,
            suburb=suburb,
            min_price=min_price,
            max_price=max_price,
            start_date=start_date,
            end_date=end_date,
            wifi=wifi,
            ac=ac,
            kitchen=kitchen,
            carpark=carpark,
            tenant_num = tenant_num,
            order_type=order_type,
        )
        return user_savelist_houses, 200

@houses.route("/recommend")
class RecommendHouses(Resource):
    @api.param("house_id", "house id for recommending houses")
    @api.param("suburb", "suburb for recommending houses")
    @api.param("price", "price for recommending houses")
    @api.param("tenant_num", "tenant num for recommending houses")
    @api.doc(description="Get houses in the user's savelist")
    def get(self):
        # get house data that used for recommender: suburb, price and tenant number
        house_id = request.args.get("house_id")
        suburb = request.args.get("suburb")
        price = request.args.get("price")
        tenant_num = request.args.get("tenant_num")
        # get recommended houses based on the house data
        recommend_houses = db.recommend_houses(house_id, suburb, price, tenant_num)
        return recommend_houses, 200
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

@savelists.route("/<string:user_id>/check/<string:house_id>")
class CheckInSavelist(Resource):
    @api.doc(description="Check if the house is in user's savelist")
    def get(self, user_id, house_id):
        user_savelist = db.find_savelist_of_user(user_id)
        # check if the house id is in user's save list
        if user_savelist:
            if house_id in user_savelist:
                return True, 200
        return False, 200

@savelists.route("/<string:user_id>/add/<string:house_id>")
class AddHouseToSavelist(Resource):
    @api.doc(description="Add house id to user's savelist")
    def get(self, user_id, house_id):
        user_savelist = db.find_savelist_of_user(user_id)
        # if ther user don't have a save list yet, create one for him/her and save the to the save list
        if user_savelist:
            if house_id not in user_savelist:
                db.add_to_user_savelist(user_id, house_id)
                return "added", 200
            else:
                return "house is already in the savelist", 400
        else:
            db.add_to_user_savelist(user_id, house_id)
            return "Created", 201

@savelists.route("/<string:user_id>/remove/<string:house_id>")
class RemoveHouseFromSavelist(Resource):
    @api.doc(description="Remove house from user's savelist")
    def get(self, user_id, house_id):
        user_savelist = db.find_savelist_of_user(user_id)
        if user_savelist:
            if house_id in user_savelist:
                db.remove_from_user_savelist(user_id, house_id)
                return "removed", 200
        return "house is not in the list", 400
# ============ user saved list part end ============


# ============ comment API part start ============
@comments.route("/<string:house_id>")
class CommentsOfHouse(Resource):
    @api.doc(description="Get full comments' info of house")
    def get(self, house_id):
        house_comments = db.find_comments_of_house(house_id)
        return house_comments, 200

@comments.route("/add")
class AddCommentToHouse(Resource):
    @api.param("house", "house's id")
    @api.param("user", "user's id")
    @api.param("content", "comment's content")
    @api.param("rating", "comment's rating")
    @api.doc(description="Add comment to house")
    def get(self):
        # get comment's data from request's query data
        house_id = request.args.get("house")
        user_id = request.args.get("user")
        content = request.args.get("content")
        rating = request.args.get("rating")
        
        # user can only comment a house once
        # house_comments = db.find_comments_of_house(house_id)
        # for comment in house_comments:
        #     if user_id == comment["user"]:
        #         return "User has posted a comment already!", 400
        
        # add comment to the house and update its rating
        if db.add_comment_to_house(house_id, user_id, content, rating):
            db.update_rating(house_id, rating)
            return "Added", 201
        else:
            return "someting is wrong, please try again later", 400
# ============ comment API part end ============

# run the app
if __name__ == "__main__":
    app.run(debug=True)

