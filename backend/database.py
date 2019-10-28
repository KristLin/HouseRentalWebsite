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
        # self.savelists = self.db['savelists']
        # self.comments = self.db['comments']

        # connect to mongoDB Atlas
        # self.dbclient = MongoClient(f'mongodb://krist:krist@9900-cluster-shard-00-00-ljnr8.mongodb.net:27017,9900-cluster-shard-00-01-ljnr8.mongodb.net:27017,9900-cluster-shard-00-02-ljnr8.mongodb.net:27017/test?ssl=true&replicaSet=9900-cluster-shard-0&authSource=admin&retryWrites=true&w=majority',  maxPoolSize=50, connect=False)
        # self.users = self.dbclient.airbnbDB.users
        # self.houses = self.dbclient.airbnbDB.houses
        # self.savelists = self.dbclient.airbnbDB.savelists
        # self.comments = self.dbclient.airbnbDB.comments

        # connect to mongoDB mlab

        # self.dbclient = MongoClient(
        #     f"mongodb://krist123:{DB_PASSWORD}@ds335678.mlab.com:35678/9900-database",
        #     123456,
        # ).get_default_database()
        
        self.dbclient = MongoClient(
            f"mongodb://krist123:{DB_PASSWORD}@ds045679.mlab.com:45679/bomb-shrimper",
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
        all_savelists = self.find_all_savelists()
        # remove house from all save lists
        for savelist in all_savelists:
            if house_id in savelist["savelist"]:
                self.remove_from_user_savelist(savelist["user"], house_id)

    def update_rating(self, house_id, rating):
        found_house = self.houses.find_one({"_id": ObjectId(house_id)})
        if "rating_num" in found_house and "rating" in found_house:
            house_rating_num = int(found_house["rating_num"])
            houes_rating = float(found_house["rating"])
            total_score = houes_rating * house_rating_num

            new_rating_num = house_rating_num + 1
            new_rating = str(round((total_score + float(rating)) / (new_rating_num), 2)
        )
        else:
            new_rating_num = 1
            new_rating = float(rating)

        query = {"_id": ObjectId(house_id)}
        return self.houses.update_one(query, {"$set": {"rating_num": new_rating_num, "rating": new_rating}})
    
    def delete_houses_of_user(self, user_id):
        cursor = self.houses.find()
        user_houses = []
        for house in cursor:
            if house["provider"] == user_id:
                user_houses.append(str(house["_id"]))
        for house_id in user_houses:
            self.delete_house(house_id)

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
            return found_list["savelist"]
        else:
            return []

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
        if found_house_comments:
            return found_house_comments["comments"]
        else:
            return []

    def add_comment_to_house(self, house_id, user_id, content, rating):
        found_house_comments = self.comments.find_one({"house": house_id})
        if found_house_comments:
            query = {"house": house_id}
            comments = found_house_comments["comments"]
            comments.append({"user": user_id, "rating": rating, "content": content})
            return self.comments.update_one(query, {"$set": {"comments": comments}})
        else:
            house_comments = {
                "house": house_id,
                "comments": [{
                    "user": user_id,
                    "content": content,
                    "rating": rating
                }]
            }
            return str(self.comments.insert_one(house_comments).inserted_id)
            
