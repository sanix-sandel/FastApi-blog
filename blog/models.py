from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.schema import ForeignKey

from .database import Base

from sqlalchemy.orm import relationship, relationships



class Blog(Base):
    __tablename__='Blog'
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    body=Column(String)
    user_id=Column(Integer, ForeignKey('User.id'))

    author=relationship("User", back_populates="blogs")


class User(Base):
    __tablename__='User'

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    email=Column(String)  
    password=Column(String)  

    blogs=relationship("Blog", back_populates="author")