from bson import ObjectId
from lib.mongo import get_mongo  # Import MongoDB connection


# Initialize MongoDB
db = get_mongo()
users_collection = db["users"]

class UserRepository:
    @staticmethod
    def create_user(user_data: dict):
        user_id = users_collection.insert_one(user_data).inserted_id
        return str(user_id)

    @staticmethod
    def get_all_users():
        return [
            {**user, "id": str(user.pop("_id"))} 
            for user in users_collection.find({}, {"password": 0})
        ]

    @staticmethod
    def get_user_by_id(user_id: str):
        user = users_collection.find_one({"_id": ObjectId(user_id)}, {"password": 0})
        return {**user, "id": str(user["_id"])} if user else None

    @staticmethod
    def update_user(user_id: str, update_data: dict):
        users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def delete_user(user_id: str):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            users_collection.delete_one({"_id": ObjectId(user_id)})
        return user

    @staticmethod
    def get_user_by_email(email: str):
        """Find user by email"""
        print(email)
        return users_collection.find_one({"email": email})