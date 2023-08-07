from sqlalchemy.orm import Session
from datetime import date
import models, schemas

#Activity
#create
def create_activity(db: Session, activity: schemas.ActivityCreate):
    db_activity = models.activity(
        activity_name = activity.activity_name,
        activity_date = activity.activity_date,
        activity_describe = activity.activity_describe
    )
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

#read
def get_activity(db: Session, activity_id: int):
    return db.query(models.activity).filter(models.activity.activity_id == activity_id).first()

#update
def update_activity(db: Session, activity_id: int, name: str , describe: str, date: date):
    update_activity = db.query(models.activity).filter(models.activity.activity_id == activity_id).first()
    update_activity.activity_name = name     
    update_activity.activity_describe = describe 
    update_activity.activity_date = date

    db.commit()
    db.refresh(update_activity)
    return update_activity

#delete
def delete_activity(db: Session, activity_id: schemas.Activity):
    activity_delete = db.query(models.activity).filter(models.activity.activity_id == activity_id).first()
    db.delete(activity_delete)
    db.commit()
    return activity_delete

#-----------------------------------------------------------------------------------------------
#TODO
#create
def create_activity_TODOs(db: Session, todo: schemas.TODOCreate, activityID: int):
    db_TODO = models.TODO(
        TODO_name = todo.TODO_name,
        A_id=activityID
    )
    db.add(db_TODO)
    db.commit()
    db.refresh(db_TODO)
    return db_TODO

#read
def get_TODO(db: Session, TODO_id: int):
    return db.query(models.TODO).filter(models.TODO.TODO_id == TODO_id).first()

#update
def update_TODO(db: Session, TODO_id: int, name: int, describe: str, date: date, Done):
    update_TODO = db.query(models.TODO).filter(models.TODO.TODO_id == TODO_id).first()
    update_TODO.TODO_name = name     
    update_TODO.TODO_describe = describe 
    update_TODO.TODO_date = date
    update_TODO.doneOrNot = Done

    db.commit()
    db.refresh(update_TODO)
    return update_TODO

#delete
def delete_TODO(db: Session, TODO_id: schemas.TODO):
    TODO_delete = db.query(models.TODO).filter(models.TODO.TODO_id == TODO_id).first()
    db.delete(TODO_delete)
    db.commit()
    return TODO_delete