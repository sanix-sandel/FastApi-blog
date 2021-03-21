from fastapi import FastAPI
from blog import  models
from blog.database import engine
from blog.routers import blog, users, login



app=FastAPI()

models.Base.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"Hello Sanick": "go to /docs"}
#
app.include_router(login.router)
app.include_router(blog.router)
app.include_router(users.router)



  

