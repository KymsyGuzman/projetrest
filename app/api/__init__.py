from fastapi import APIRouter
from app.api.movies import router as movies_router
from app.api.theaters import router as theaters_router

router = APIRouter()

router.include_router(movies_router, prefix="/movies", tags=["movies"])
router.include_router(theaters_router, prefix="/theaters", tags=["theaters"])