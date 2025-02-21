from fastapi import APIRouter
from controllers.portfolio import router as portfolio_router

portfolio_routes = APIRouter()
portfolio_routes.include_router(portfolio_router, prefix="/portfolio")

