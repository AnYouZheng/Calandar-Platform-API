from sqlalchemy.orm import Session
import models, schemas

#Activity
def get_activity(db: Session, activity_id: int):
    return db.query(models.activity).filter(models.activity.activity_id == activity_id).first()


def get_activity_by_id(db: Session, id: int):
    return db.query(models.activity).filter(models.activity.activity_id == id).first()


def get_activitys(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.activity).offset(skip).limit(limit).all()


def create_activity(db: Session, user: schemas.ActivityCreate):
    db_activity = models.activity()
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity