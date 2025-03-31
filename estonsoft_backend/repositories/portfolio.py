from bson import ObjectId
from lib.mongo import get_mongo
db = get_mongo()

class PortfolioRepository:
    collection = db["portfolios"]

    @staticmethod
    def create(portfolio_data: dict):
        return PortfolioRepository.collection.insert_one(portfolio_data).inserted_id

    @staticmethod
    def get_all():
        return list(PortfolioRepository.collection.find())

    @staticmethod
    def get_by_id(portfolio_id: str):
        return PortfolioRepository.collection.find_one({"_id": ObjectId(portfolio_id)})

    @staticmethod
    def update(portfolio_id: str, updated_data: dict):
        return PortfolioRepository.collection.update_one({"_id": ObjectId(portfolio_id)}, {"$set": updated_data})

    @staticmethod
    def delete(portfolio_id: str):
        return PortfolioRepository.collection.delete_one({"_id": ObjectId(portfolio_id)})
