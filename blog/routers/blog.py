from fastapi import APIRouter
from typing import List
from .. import schemas,  models, database
from fastapi import (
    Depends, status, Response,
    HTTPException
)
from sqlalchemy.orm import Session
from ..repository import blog


router=APIRouter(
        prefix="/blog",
        tags=["blogs"]
    )




#BLOG
@router.post('/', status_code=status.HTTP_201_CREATED )
def create(request: schemas.Blog, db:Session=Depends(database.get_db)):
    return blog.create(request, db)



@router.get('/', response_model=List[schemas.ShowBlog] )
def all(db:Session=Depends(database.get_db)):
    return blog.get_all(db)    



@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog )
def show(id, db:Session=Depends(database.get_db)):
    return blog.show(id,db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT )
def destroy(id, db:Session=Depends(database.get_db)):
    return blog.destroy(id,db)



@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED )
def update(id, request:schemas.Blog, db:Session=Depends(database.get_db)):
    return blog.update(id,request, db)