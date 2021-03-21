from pydantic import BaseModel
from typing import List, Optional

class Blog(BaseModel):
    title:str
    body:str

class BlogNew(Blog):
    class Config():
        orm_mode=True

class User(BaseModel):
    name:str
    email:str
    password:str

  
class ShowUser(BaseModel):
    name:str
    email:str    
    blogs: List[BlogNew]
    class Config():
        orm_mode=True


class ShowBlog(Blog):

    title: str
    body: str 
    author:ShowUser

    class Config():
        orm_mode=True        



class Login(BaseModel):
    username:str
    password:str        

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None    