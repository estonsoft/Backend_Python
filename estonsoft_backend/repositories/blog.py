from bson import ObjectId
from datetime import datetime
from lib.mongo import get_mongo  # ✅ Import get_mongo()

# Initialize database instance
db = get_mongo()

class BlogRepository:
    collection = db.blog  # ✅ Correct way to access MongoDB collection

    @staticmethod
    def create(blog_post: dict):
        blog_post["timestamp"] = datetime.now().isoformat()
        result = BlogRepository.collection.insert_one(blog_post)
        blog_post["id"] = str(result.inserted_id)
        return blog_post

    @staticmethod
    def get_all():
        return [{**post, "id": str(post.pop("_id"))} for post in BlogRepository.collection.find()]

    @staticmethod
    def get_by_id(post_id: str):
        post_object_id = ObjectId(post_id)
        post = BlogRepository.collection.find_one({"_id": post_object_id})
        return {**post, "id": str(post.pop("_id"))} if post else None

    @staticmethod
    def update(post_id: str, update_data: dict):
        post_object_id = ObjectId(post_id)
        BlogRepository.collection.update_one({"_id": post_object_id}, {"$set": update_data})
        return BlogRepository.get_by_id(post_id)

    @staticmethod
    def delete(post_id: str):
        post_object_id = ObjectId(post_id)
        post = BlogRepository.get_by_id(post_id)
        if post:
            BlogRepository.collection.delete_one({"_id": post_object_id})
        return post
