from pydantic import BaseModel

#Activity

class ActivityBase(BaseModel):
    id: int
    title: str
    description: str | None = None

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):
        
    class Config:
        orm_mode = True

#TODO

class TODOBase(BaseModel):
    title: str
    describtion: str

class TODOCreate(TODOBase):
    pass
   
class TODO(TODOBase):
    id: int
    
    class Config:
        orm_mode = True