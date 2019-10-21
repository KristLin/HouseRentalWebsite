
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

# Database to manipulate user & house data
load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")


class DB(object):
    def __init__(self):
        # self.dbclient = MongoClient(host='mongodb://useradmin:useradmin1@ds257752.mlab.com:57752/ass2')

        # connect to local mongoDB
        # self.dbclient = MongoClient('mongodb://localhost:27017/')
        # self.db = self.dbclient['airbnbDB']
        # self.users = self.db['users']
        # self.houses = self.db['houses']

        # connect to mongoDB Atlas
        # self.dbclient = MongoClient(f'mongodb://krist:{DB_PASSWORD}@9900-cluster-shard-00-00-ljnr8.mongodb.net:27017,9900-cluster-shard-00-01-ljnr8.mongodb.net:27017,9900-cluster-shard-00-02-ljnr8.mongodb.net:27017/test?ssl=true&replicaSet=9900-cluster-shard-0&authSource=admin&retryWrites=true&w=majority',  maxPoolSize=50, connect=False)
        # self.users = self.dbclient.airbnbDB.users
        # self.houses = self.dbclient.airbnbDB.houses

        # connect to mongoDB mlab
        
        self.dbclient = MongoClient(f"mongodb://krist123:{DB_PASSWORD}@ds335678.mlab.com:35678/9900-database", 123456).get_default_database()
        self.users = self.dbclient["users"]
        self.houses = self.dbclient["houses"]
        super().__init__()

    # =========== user data manipulation ===========
    def find_user_by_id(self, user_id):
        found_user = self.users.find_one({"_id": ObjectId(user_id)})
        if found_user:
            found_user["_id"] = str(found_user["_id"])
        return found_user

    def find_user_by_email(self, email):
        found_user = self.users.find_one({"email": email})
        if found_user:
            found_user["_id"] = str(found_user["_id"])
        return found_user

    def find_all_users(self):
        cursor = self.users.find()
        all_users = []
        for user in cursor:
            user['_id'] = str(user['_id'])
            all_users.append(user)
        return all_users

    def add_user(self, user):
        _id = str(self.users.insert_one(user).inserted_id)
        return _id

    # update & delete need to return a flag
    def update_user(self, user_id, update_info):
        query = {"_id": ObjectId(user_id)}
        return self.users.update_one(query, {"$set": update_info})

    def delete_user(self, user_id):
        self.users.delete_one({"_id": ObjectId(user_id)})

    # =========== house data manipulation ===========
    def find_house_by_id(self, house_id):
        found_house = self.houses.find_one({"_id": ObjectId(house_id)})
        if found_house:
            # change the ObjectId to string format
            found_house['_id'] = str(found_house['_id'])
        return found_house

    def find_random_houses(self):
        cursor = self.houses.find()
        all_houses = []
        for house in cursor:
            house['_id'] = str(house['_id'])
            all_houses.append(house)
        random_houses = all_houses[:3]
        return random_houses

    def find_all_houses(self):
        cursor = self.houses.find()
        all_houses = []
        for house in cursor:
            house['_id'] = str(house['_id'])
            all_houses.append(house)
        return all_houses

    def find_user_houses(self, user_id):
        cursor = self.houses.find()
        all_houses = []
        for house in cursor:
            if house["provider"] == user_id:
                house['_id'] = str(house['_id'])
                all_houses.append(house)
        return all_houses

    def add_house(self, house):
        _id = str(self.houses.insert_one(house).inserted_id)
        return _id

    def update_house(self, house_id, update_info):
        query = {"_id": ObjectId(house_id)}
        return self.houses.update_one(query, {"$set": update_info})

    def delete_house(self, house_id):
        self.houses.delete_one({'_id': ObjectId(house_id)})
