from bson import ObjectId
from datetime import datetime
from lib.mongo import get_mongo  # ✅ Import get_mongo()

# Initialize database instance
db = get_mongo()

class TestimonialRepository:
    collection = db.testimonial  # ✅ Correct way to access MongoDB collection

    @staticmethod
    def create(testimonial_post: dict):
        testimonial_post["timestamp"] = datetime.now().isoformat()
        result = TestimonialRepository.collection.insert_one(testimonial_post)
        testimonial_post["id"] = str(result.inserted_id)
        return testimonial_post

    @staticmethod
    def get_all():
        return [{**post, "id": str(post.pop("_id"))} for post in TestimonialRepository.collection.find()]

    @staticmethod
    def get_by_id(post_id: str):
        post_object_id = ObjectId(post_id)
        post = TestimonialRepository.collection.find_one({"_id": post_object_id})
        return {**post, "id": str(post.pop("_id"))} if post else None

    @staticmethod
    def update(post_id: str, update_data: dict):
        post_object_id = ObjectId(post_id)
        TestimonialRepository.collection.update_one({"_id": post_object_id}, {"$set": update_data})
        return TestimonialRepository.get_by_id(post_id)

    @staticmethod
    def delete(post_id: str):
        post_object_id = ObjectId(post_id)
        post = TestimonialRepository.get_by_id(post_id)
        if post:
            TestimonialRepository.collection.delete_one({"_id": post_object_id})
        return post
