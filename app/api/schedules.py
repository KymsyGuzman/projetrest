from fastapi import APIRouter, Depends, HTTPException, status

#from db.models import Schedule
#from app.db.database import get_db
#from app.core.auth import get_current_active_user
from sqlalchemy.orm import Session
from app.db.models import Schedule
from app.db.database import get_db
from app.core.auth import get_current_active_user
router = APIRouter()

@router.post("/schedules")
async def create_schedule(schedule: Schedule, db=Depends(get_db), current_user=Depends(get_current_active_user)):
    db.add(schedule)
    db.commit()
    db.refresh(schedule)
    return schedule

@router.put("/schedules/{schedule_id}")
#async def update_schedule(schedule_id: int, schedule: Schedule, db=Depends(get_db), current_user=Depends(get_current_active_user)):

async def update_schedule(
    schedule_id: int, 
    schedule: Schedule, 
    db: Session = Depends(get_db), 
    current_user=Depends(get_current_active_user)):
    
    # Recherche l'horaire existant
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    
    # Si l'horaire n'existe pas, retourne une erreur 404
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    
    # Mise à jour des champs de l'horaire
    for field, value in schedule.dict().items():
        setattr(db_schedule, field, value)
    
    # Commit les changements à la base de données
    db.commit()

    return db_schedule
@router.delete("/schedules/{schedule_id}")
#async def delete_schedule(schedule_id: int, db=Depends(get_db), current_user=Depends(get_current_active_user)):
async def delete_schedule(
    schedule_id: int, 
    db: Session = Depends(get_db), 
    current_user=Depends(get_current_active_user)):
    
    # Recherche l'horaire existant
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    
    # Si l'horaire n'existe pas, retourne une erreur 404
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")

    # Supprime l'horaire de la base de données
    db.delete(db_schedule)

    # Commit les changements à la base de données
    db.commit()

    return {"detail": "Schedule deleted"}

