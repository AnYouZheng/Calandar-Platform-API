from sqlalchemy import ForeignKey, Null, Boolean, Column, Date, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

#創建 table:activity 
class activity(Base):
    __tablename__ = 'Activitys'
    activity_id   = Column(Integer, primary_key=True)
    activity_name = Column(String,  unique=True)
    activity_date = Column(Date)
    activity_describe = Column(String, index = True)

    T_id   = Column(Integer, ForeignKey("TODO.TODO_id"))

#創建 table:TODO   
class TODO(Base):
    __tablename__ = 'TODOs'
    TODO_id     =   Column(Integer, primary_key=True)
    TODO_name   =   Column(String,  unique=True)
    TODO_date   =   Column(Date)
    doneOrNot   =   Column(Boolean, default= False)
    TODO_descripe = Column(String, index = True)

    A_id    = Column(Integer, ForeignKey("activity.activity_id"))