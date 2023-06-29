from sqlalchemy import Boolean, Column, Date, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

#創建 table:activity 
class activity(Base):
    __tablename__ = 'activity'
    activity_id:    Column(Integer, primary_key=True)
    activity_name:  Column(String,  unique=True)
    activity_date:  Column(Date)

#創建 table:TODO   
class TODO(Base):
    __tablename__ = 'TODO'
    TODO_id:    Column(Integer, primary_key=True)
    TODO_name:  Column(String,  unique=True)
    TODO_date:  Column(Date)
    doneOrNot:  Column(Boolean)