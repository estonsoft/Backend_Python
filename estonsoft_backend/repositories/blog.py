from bson import ObjectId
from datetime import datetime
from lib.mongo import get_mongo

db = get_mongo()

class BlogRepository:
    collection = db["blogs"]

    @staticmethod
    def create(blog_data: dict):
        blog_data["timestamp"] = datetime.utcnow().isoformat()
        result = BlogRepository.collection.insert_one(blog_data)
        return str(result.inserted_id)

    @staticmethod
    def update(blog_id: str, update_data: dict):
        print(update_data)
        return BlogRepository.collection.update_one({"_id": ObjectId(blog_id)}, {"$set": update_data})


    @staticmethod
    def delete(blog_id: str):
        return BlogRepository.collection.delete_one({"_id": ObjectId(blog_id)})

    @staticmethod
    def get_all():
        return list(BlogRepository.collection.find())

    @staticmethod
    def get_by_id(blog_id: str):
        return BlogRepository.collection.find_one({"_id": ObjectId(blog_id)})
