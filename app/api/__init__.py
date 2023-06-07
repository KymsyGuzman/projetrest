from fastapi import APIRouter
#from app.api.movies import router as movies_router
#from app.api.theaters import router as theaters_router
from app.api import schedules
from app.api import movies
from app.api import theaters
router = APIRouter()

#router.include_router(movies_router, prefix="/movies", tags=["movies"])
#router.include_router(theaters_router, prefix="/theaters", tags=["theaters"])
router.include_router(theaters.router, prefix="/theaters", tags=["theaters"])
router.include_router(movies.router, prefix="/theaters", tags=["movies"])
router.include_router(schedules.router, prefix="/schedules", tags=["schedules"])








