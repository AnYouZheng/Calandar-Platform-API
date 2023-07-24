from sqlalchemy import Boolean, Column, Date, Integer, String
from database import Base

#創建 table:activity 
class activity(Base):
    __tablename__ = 'Activities'
    activity_id   = Column(Integer, primary_key=True)
    activity_name = Column(String(12))
    activity_date = Column(Date)
    activity_describe = Column(String(50), index = True)

#創建 table:TODO   
class TODO(Base):
    __tablename__ = 'TODOs'
    TODO_id     =   Column(Integer, primary_key=True)
    TODO_name   =   Column(String(12),  unique=True)
    TODO_date   =   Column(Date)
    TODO_descripe = Column(String(50), index = True)
    doneOrNot   =   Column(Boolean, default= False)
    A_id        =   Column(Integer)