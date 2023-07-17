from sqlalchemy.orm import Session
from datetime import date
import models, schemas

#Activity
def get_activity(db: Session, activity_id: int):
    return db.query(models.activity).filter(models.activity.activity_id == activity_id).first()


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

#TODO
def get_TODO(db: Session, TODO_id: int):
    return db.query(models.TODO).filter(models.TODO.TODO_id == TODO_id).first()


def create_TODO(db: Session, TODO: schemas.TODOCreate):
    db_TODO = models.TODO(
        TODO_name = TODO.TODO_name,
        TODO_date = TODO.TODO_date,
        TODO_describe = TODO.TODO_describe
    )
    db.add(db_TODO)
    db.commit()
    db.refresh(db_TODO)
    return db_TODO