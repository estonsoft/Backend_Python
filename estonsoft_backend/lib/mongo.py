import os
from pymongo import MongoClient

# MongoDB Connection
_client = None
_db = None

MONGO_URI = os.getenv("MONGO_URI")
print("mongo uri", MONGO_URI)

def connect_mongo():
    global _client, _db
    if _client is None:
        _client = MongoClient(MONGO_URI)  # ✅ Initialize only once
        _db = _client["rbac"]  # ✅ Get database instance
    return _client  # ✅ Return client for manual operations if needed

def get_mongo():
    global _db
    if _db is None:
        connect_mongo()  # Ensure database is initialized
    return _db  # ✅ Now you can import and use `get_mongo()`


db = get_mongo()
users_collection = db["users"]
portfolio_collection = db["portfolios"]
testimonial_collection = db["testimonials"]