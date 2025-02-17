from fastapi import FastAPI
import uvicorn
import os
from .config import setup_cors
from .routes import router

app = FastAPI()
setup_cors(app)

# Include routes
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
