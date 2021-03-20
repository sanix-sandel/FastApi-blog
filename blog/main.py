from fastapi import (
    FastAPI, Depends, status, Response,
    HTTPException
)
from passlib.utils.decor import deprecated_method
from . import schemas, models, hashing
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List


myapp=FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()    

@myapp.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db:Session=Depends(get_db)):
    new_blog=models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 


@myapp.get('/blog', response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs    

@myapp.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
       # response.status_code=status.HTTP_404_NOT_FOUND
        #return {'detail':f'Blog with id {id} is not avaialable'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with id {id} is not avaialable')
    return blog


@myapp.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return 'done'

@myapp.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Blog, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with id {id} not found")
    blog.update({"title":request.title, "body":request.body})                         
    db.commit()
    return "update" 


@myapp.post('/users')
def create_user(request: schemas.User, db:Session=Depends(get_db)):
   
    new_user=models.User(name=request.name, 
                            email=request.email, 
                            password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user    