from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn

import crud, models, schemas
from datetime import date
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


@app.post("/Create activity/", response_model=schemas.Activity)
def create_Activity(activity: schemas.ActivityCreate, db: Session = Depends(get_db)):
    activity_create= crud.create_activity(db=db, activity=activity)
    return(activity_create)


@app.get("/Search activities/{activity_id}", response_model=schemas.Activity)
def read_Activity(activity_id: int, db: Session = Depends(get_db)):
    db_activity = crud.get_activity(db, activity_id = activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return (db_activity)


@app.update("/Update exsisted activity/", response_model=schemas.Activity)
def update_Activity(activity_id: int, name: str , describe: str, date: date, db: Session = Depends(get_db)):
    db_activity = crud.get_activity(db, activity_id = activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    activity_update = crud.update_activity(db, activity_id= activity_id, name= name, describe=describe, date=date)
    return (activity_update)
        
# @app.delete("/Delete activity/", reponse_model=schemas.Activity)
def delete_Activity(activity_id: int, db: Session = Depends(get_db)):
    db_activity = crud.get_activity(db, activity_id = activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    activity_delete = crud.delete_activity(db, activity_id = activity_id)
    return (activity_delete)
    

@app.post("/Create TODO with Activities/{activity_id}/TODOs/", response_model=schemas.TODO)
def create_activity_TODOs(
    activity_id: int, todo: schemas.TODOCreate, db: Session = Depends(get_db)
):
    return crud.create_activity_TODOs(db=db, todo= todo, activity_id=activity_id)


@app.get("/Search TODOs/{TODO_id}", response_model=schemas.TODO)
def read_TODO(TODO_id: int, db: Session = Depends(get_db)):
    db_TODO = crud.get_TODO(db, TODO_id = TODO_id)
    if db_TODO is None:
        raise HTTPException(status_code=404, detail="TODO not found")
    return db_TODO


@app.update("/Update exsisted TODO/", response_model=schemas.TODO)
def update_TODO(TODO_id: int, name: str , describe: str, date: date, db: Session = Depends(get_db)):
    db_TODO = crud.get_TODO(db, TODO_id = TODO_id)
    if db_TODO is None:
        raise HTTPException(status_code=404, detail="TODO not found")
    TODO_update = crud.update_TODO(db, TODO_id= TODO_id, name= name, describe=describe, date=date)
    return (TODO_update)
        
@app.delete("/Delete TODO/", reponse_model=schemas.TODO)
def delete_TODO(TODO_id: int, db: Session = Depends(get_db)):
    db_TODO = crud.get_TODO(db, TODO_id = TODO_id)
    if db_TODO is None:
        raise HTTPException(status_code=404, detail="TODO not found")
    TODO_delete = crud.delete_TODO(db, TODO_id = TODO_id)
    return (TODO_delete)
   

if __name__ == '__main__' :
    uvicorn.run("main:app")