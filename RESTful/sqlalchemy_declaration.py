from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parent'
    #declare parent columns
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    children = relationship("Child", back_populates="parent")

class Child(Base):
    __tablename__ = 'child'
    #declare child columns
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="children")

#create engine to store data in sqlite DB
engine = create_engine('sqlite:///parent_child.db')

#create tables in engine
Base.metadata.create_all(engine)
