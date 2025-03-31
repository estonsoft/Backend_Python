from fastapi import FastAPI
import uvicorn
import os
from routes.routes import router
from lib.mongo import connect_mongo, get_mongo  # ✅ Ensure MongoDB is initialized
from lib.cors import setup_cors
from services.user import UserService


# Initialize MongoDB client before using it
connect_mongo()  # ✅ Ensure MongoDB is ready before FastAPI starts

# Initialize FastAPI
app = FastAPI()
setup_cors(app)

# Include routes
UserService.initialize_admin()  # ✅ Create admin if not exists

app.include_router(router)

# Ensure DB is initialized
db = get_mongo()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
