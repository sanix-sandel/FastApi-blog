from fastapi import FastAPI
from passlib.utils.decor import deprecated_method
from . import models 
from .database import engine

from .routers import blog, users, login



myapp=FastAPI()

models.Base.metadata.create_all(engine)

myapp.include_router(login.router)
myapp.include_router(blog.router)
myapp.include_router(users.router)



  

