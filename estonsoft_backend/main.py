from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
from routes.blog import router
from lib.mongo import connect_mongo  # ✅ Ensure MongoDB is initialized
from lib.cors import setup_cors

# Load environment variables
load_dotenv()

# Initialize MongoDB client before using it
connect_mongo()  # ✅ Ensure MongoDB is ready before FastAPI starts

# Initialize FastAPI
app = FastAPI()
setup_cors(app)

# Include routes
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
