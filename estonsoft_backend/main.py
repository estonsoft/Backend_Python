import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables BEFORE any other imports
dotenv_path = find_dotenv()
print("📌 dotenv_path found at:", dotenv_path)

if not load_dotenv(dotenv_path):
    print(f"⚠️ Warning: Could not load .env file from {dotenv_path}")

# Debugging: Print environment variables
print(f"MONGO_CONNECTION_STRING={os.getenv('MONGO_CONNECTION_STRING')}")
print(f"SECRET_KEY={os.getenv('SECRET_KEY')}")
print(f"ALLOWED_ORIGINS={os.getenv('ALLOWED_ORIGINS')}")

# Now, import everything else that depends on env variables
from fastapi import FastAPI
import uvicorn
from routes.routes import router
from lib.mongo import connect_mongo, get_mongo
from lib.cors import setup_cors
from services.user import UserService

# Ensure the values exist
required_envs = ["MONGO_CONNECTION_STRING", "SECRET_KEY", "ALLOWED_ORIGINS"]
missing_envs = [var for var in required_envs if not os.getenv(var)]

if missing_envs:
    raise RuntimeError(f"❌ Missing environment variables: {', '.join(missing_envs)}")

print("✅ Environment variables loaded successfully!")

# Initialize MongoDB client before using it
connect_mongo()

# Initialize FastAPI
app = FastAPI()
setup_cors(app)

# Include routes
UserService.initialize_admin()
app.include_router(router)

# Ensure DB is initialized
db = get_mongo()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
