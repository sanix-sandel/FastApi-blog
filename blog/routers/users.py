from fastapi import APIRouter
from typing import List
from .. import schemas,  models, database, hashing
from fastapi import Depends
from sqlalchemy.orm import Session
from ..repository import users



router=APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db:Session=Depends(database.get_db)):
    return users.create(request,db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session=Depends(database.get_db)):
    return users.show(id,db)