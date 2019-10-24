from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

# Database to manipulate user & house data
load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")


class DB(object):
    def __init__(self):

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

        self.dbclient = MongoClient(
            f"mongodb://krist123:{DB_PASSWORD}@ds335678.mlab.com:35678/9900-database",
            123456,
        ).get_default_database()
        self.users = self.dbclient["users"]
        self.houses = self.dbclient["houses"]
        self.savelists = self.dbclient["savelists"]
        self.comments = self.dbclient["comments"]
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
            user["_id"] = str(user["_id"])
            all_users.append(user)
        return all_users

    def add_user(self, user):
        _id = str(self.users.insert_one(user).inserted_id)
        return _id

    # update & delete need to return a flag
    def update_user(self, user_id, update_info):
        query = {"_id": ObjectId(user_id)}
        return self.users.update_one(query, {"$set": update_info})

    def update_user_profile(self, user_id, update_profile):
        query = {"_id": ObjectId(user_id)}
        return self.users.update_one(query, {"$set": {"profile": update_profile}})

    def delete_user(self, user_id):
        self.users.delete_one({"_id": ObjectId(user_id)})

    # =========== house data manipulation ===========
    def find_house_by_id(self, house_id):
        found_house = self.houses.find_one({"_id": ObjectId(house_id)})
        if found_house:
            # change the ObjectId to string format
            found_house["_id"] = str(found_house["_id"])
        return found_house

    def find_random_houses(self):
        cursor = self.houses.find()
        all_houses = []
        for house in cursor:
            house["_id"] = str(house["_id"])
            all_houses.append(house)
        random_houses = all_houses[:3]
        return random_houses

    def find_all_houses(self):
        cursor = self.houses.find()
        all_houses = []
        for house in cursor:
            house["_id"] = str(house["_id"])
            all_houses.append(house)
        return all_houses

    def find_user_houses(self, user_id):
        cursor = self.houses.find()
        user_houses = []
        for house in cursor:
            if house["provider"] == user_id:
                house["_id"] = str(house["_id"])
                user_houses.append(house)
        return user_houses

    def find_savelist_houses(self, house_id_list):
        cursor = self.houses.find()
        savelist_houses = []
        for house in cursor:
            if str(house["_id"]) in house_id_list:
                house["_id"] = str(house["_id"])
                savelist_houses.append(house)
        return savelist_houses

    def add_house(self, house):
        _id = str(self.houses.insert_one(house).inserted_id)
        return _id

    def update_house(self, house_id, update_info):
        query = {"_id": ObjectId(house_id)}
        return self.houses.update_one(query, {"$set": update_info})

    def delete_house(self, house_id):
        self.houses.delete_one({"_id": ObjectId(house_id)})

    def update_rating(self, house_id, rating):
        found_house = self.houses.find_one({"_id": ObjectId(house_id)})

        house_rating_num = int(found_house["rating_num"])
        houes_rating = float(found_house["rating"])

        new_rating = str(
            round(
                (houes_rating * house_rating_num + float(rating))
                / (house_rating_num + 1),
                2,
            )
        )
        new_rating_num = str(house_rating_num + 1)
        query = {"_id": ObjectId(house_id)}
        return self.houses.update_one(
            query, {"$set": {"rating_num": new_rating_num, "rating": new_rating}}
        )

    # =========== save list data manipulation ===========
    def find_all_savelists(self):
        cursor = self.savelists.find()
        all_savelists = []
        for savelist in cursor:
            savelist["_id"] = str(savelist["_id"])
            all_savelists.append(savelist)
        return all_savelists

    def find_savelist_of_user(self, user_id):
        found_list = self.savelists.find_one({"user": user_id})
        if found_list:
            # change the ObjectId to string format
            found_list["_id"] = str(found_list["_id"])
        return found_list

    def add_to_user_savelist(self, user_id, house_id):
        found_list = self.savelists.find_one({"user": user_id})
        if found_list:
            query = {"user": user_id}
            savelist = found_list["savelist"]
            savelist.append(house_id)
            return self.savelists.update_one(query, {"$set": {"savelist": savelist}})
        else:
            savelist = {"user": user_id, "savelist": [house_id]}
            return str(self.savelists.insert_one(savelist).inserted_id)
    
    def remove_from_user_savelist(self, user_id, house_id):
        found_list = self.savelists.find_one({"user": user_id})
        query = {"user": user_id}
        savelist = found_list["savelist"]
        savelist.remove(house_id)
        return self.savelists.update_one(query, {"$set": {"savelist": savelist}})

    # =========== comments data manipulation ===========
    def find_comments_of_house(self, house_id):
        found_house_comments = self.comments.find_one({"house": house_id})
        return found_house_comments

    def add_comment_to_house(self, house_id, user_id, new_comment):
        found_house_comments = self.comments.find_one({"house": house_id})
        if found_house_comments:
            query = {"house": ObjectId(house_id)}
            comments = found_house_comments["comments"]
            comments.append({"user": user_id, "content": new_comment})
            return self.comments.update_one(query, {"$set": {"comments": comments}})
