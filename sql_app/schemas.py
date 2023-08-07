from typing import Optional
from pydantic import BaseModel
from datetime import date

#Activity

class ActivityBase(BaseModel):
    activity_name: str

class ActivityCreate(ActivityBase):
    activity_date: date
    activity_describe: Optional[str] = None
    
class Activity(ActivityBase):
    activity_id: int
    
    class Config:
        orm_mode = True
        

#TODO

class TODOBase(BaseModel):
    TODO_name: str
    A_id: int

class TODOCreate(TODOBase):
    TODO_date: date
    TODO_describe: Optional[str] = None

class TODO(TODOBase):
    TODO_id: int
 
    class Config:
        orm_mode = True