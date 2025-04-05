from fastapi import APIRouter
from controllers.blog import router as blog_router
from controllers.user import router as user_router
from controllers.auth import router as auth_router
from controllers.portfolio import router as portfolio_router
from controllers.testimonials import router as testimonials_router
from controllers.healthcheck import router as healthcheck_routers

router = APIRouter()
router.include_router(healthcheck_routers)
router.include_router(blog_router)
router.include_router(user_router)
router.include_router(auth_router)
router.include_router(portfolio_router)
router.include_router(testimonials_router)


