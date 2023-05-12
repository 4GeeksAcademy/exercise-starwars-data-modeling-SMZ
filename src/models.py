import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    elenco = Column(String(250), nullable=False)
    height = Column(String(30), nullable=False)
    mass = Column(String(30), nullable=False)
    hair_color = Column(String(30), nullable=False)
    skin_color = Column(String(30), nullable=False)
    eye_color = Column(String(30), nullable=False)
    birth_year = Column(String(30), nullable=False)
    gender = Column(String(30), nullable=False)
    created = Column(String(30), nullable=False)
    edited = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    homeworld = Column(String(30), nullable=False)
    url = Column(String(250), nullable=False)

class Films(Base):
    __tablename__ = 'films'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    #street_name = Column(String(250))
    #street_number = Column(String(250))
    #post_code = Column(String(250), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)
    elenco = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    planets = Column(String(250), nullable=False)
    starships = Column(String(250), nullable=False)
    vehicles = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    created = Column(String(30), nullable=False)
    edited = Column(String(30), nullable=False)
    producer = Column(String(30), nullable=False)
    title = Column(String(30), nullable=False)
    episode_id = Column(String(30), nullable=False)
    director = Column(String(30), nullable=False)
    release_date = Column(String(30), nullable=False)
    opening_crawl = Column(String(250), nullable=False)
    url = Column(String(30), nullable=False)
    people_id = Column(Integer, ForeignKey(People.id))

class vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    characters = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
