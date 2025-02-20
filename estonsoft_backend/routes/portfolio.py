from fastapi import APIRouter
from controllers.portfolio import router as portfolio_router

router = APIRouter()
router.include_router(portfolio_router, prefix="/portfolio")

