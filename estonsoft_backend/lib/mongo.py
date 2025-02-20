import os
from pymongo import MongoClient

# Global variables to store MongoDB client and database
_client = None
_db = None

def connect_mongo():
    """
    Initializes and returns the MongoDB client. Ensures it is only created once.
    """
    global _client, _db
    if _client is None:
        MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        DB_NAME = os.getenv("DB_NAME", "estonsoft")
        _client = MongoClient(MONGO_URI)  # ✅ Initialize only once
        _db = _client[DB_NAME]  # ✅ Get database instance
    return _client  # ✅ Return client for manual operations if needed

def get_mongo():
    """
    Returns the MongoDB database instance.
    Ensures `connect_mongo()` is called before accessing `_db`.
    """
    global _db
    if _db is None:
        connect_mongo()  # Ensure database is initialized
    return _db  # ✅ Now you can import and use `get_mongo()`
