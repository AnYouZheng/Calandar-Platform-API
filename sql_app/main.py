from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/activity/", response_model=schemas.Activity)
def create_Activity(activity: schemas.ActivityCreate, db: Session = Depends(get_db)):
    db_activity = crud.get_activity_by_id(db, id = activity.id)
    if db_activity:
        raise HTTPException(status_code=400, detail="the activity is created!")
    return crud.create_activity(db=db, id = id)


@app.get("/Activitys/{activity_id}", response_model=schemas.Activity)
def read_Activity(activity_id: int, db: Session = Depends(get_db)):
    db_activity = crud.get_activity(db, activity_id = activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return db_activity

if __name__ == '__main__' :
    uvicorn.run("main:app")