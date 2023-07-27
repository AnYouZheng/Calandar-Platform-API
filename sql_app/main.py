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
    create= crud.create_activity(db=db, activity=activity)
    return(create)


@app.get("/Activities/{activity_id}", response_model=schemas.Activity)
def read_Activity(activity_id: int, db: Session = Depends(get_db)):
    db_activity = crud.get_activity(db, activity_id = activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return db_activity


@app.post("/Actvities/{activity_id}/TODOs/", response_model=schemas.TODO)
def create_activity_TODOs(
    activity_id: int, todo: schemas.TODOCreate, db: Session = Depends(get_db)
):
    return crud.create_activity_TODOs(db=db, todo= todo, activity_id=activity_id)


@app.get("/TODOs/{TODO_id}", response_model=schemas.TODO)
def read_TODO(TODO_id: int, db: Session = Depends(get_db)):
    db_TODO = crud.get_TODO(db, TODO_id = TODO_id)
    if db_TODO is None:
        raise HTTPException(status_code=404, detail="TODO not found")
    return db_TODO


if __name__ == '__main__' :
    uvicorn.run("main:app")