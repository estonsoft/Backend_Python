from bson import ObjectId
from datetime import datetime
from lib.mongo import get_mongo  # ✅ Import get_mongo()

# Initialize database instance
db = get_mongo()

class PortfolioRepository:
    collection = db.portfolio  # ✅ Correct way to access MongoDB collection

    @staticmethod
    def create(portfolio_post: dict):
        portfolio_post["timestamp"] = datetime.now().isoformat()
        result = PortfolioRepository.collection.insert_one(portfolio_post)
        portfolio_post["id"] = str(result.inserted_id)
        return portfolio_post

    @staticmethod
    def get_all():
        return [{**post, "id": str(post.pop("_id"))} for post in PortfolioRepository.collection.find()]

    @staticmethod
    def get_by_id(post_id: str):
        post_object_id = ObjectId(post_id)
        post = PortfolioRepository.collection.find_one({"_id": post_object_id})
        return {**post, "id": str(post.pop("_id"))} if post else None

    @staticmethod
    def update(post_id: str, update_data: dict):
        post_object_id = ObjectId(post_id)
        PortfolioRepository.collection.update_one({"_id": post_object_id}, {"$set": update_data})
        return PortfolioRepository.get_by_id(post_id)

    @staticmethod
    def delete(post_id: str):
        post_object_id = ObjectId(post_id)
        post = PortfolioRepository.get_by_id(post_id)
        if post:
            PortfolioRepository.collection.delete_one({"_id": post_object_id})
        return post
