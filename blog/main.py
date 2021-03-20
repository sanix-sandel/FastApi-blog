from fastapi import FastAPI, Depends
from . import schemas, models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session


myapp=FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()    

@myapp.post('/blog')
def create(request: schemas.Blog, db:Session=Depends(get_db)):
    new_blog=models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 


@myapp.get('/blog')
def all(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs    