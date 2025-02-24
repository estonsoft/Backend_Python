from fastapi import APIRouter
from controllers.testimonial import router as testimonial_router

testimonial_routes = APIRouter()
testimonial_routes.include_router(testimonial_router, prefix="/testimonial")

