import os
import jwt
from fastapi import HTTPException, Header
from lib.mongo import get_mongo  # Import MongoDB connection

# Load secret key from environment
SECRET_KEY = os.getenv("SECRET_KEY")

# Get users collection
db = get_mongo()
users_collection = db["users"]

def generate_token(email: str) -> str:
    """
    Generate a JWT token with the given email (No expiry).
    """
    payload = {"email": email}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_token(authorization: str = Header(None)):
    """
    Verify JWT token and return user details.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="❌ Access token required")
    
    try:
        payload = jwt.decode(authorization, SECRET_KEY, algorithms=["HS256"])
        user = users_collection.find_one({"email": payload["email"]})
        if not user:
            raise HTTPException(status_code=401, detail="❌ Invalid token, user not found")
        return user
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="❌ Invalid token")
