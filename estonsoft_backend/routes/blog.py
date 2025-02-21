from fastapi import APIRouter
from controllers.blog import router as blog_router

blog_routes = APIRouter()
blog_routes.include_router(blog_router, prefix="/post")

