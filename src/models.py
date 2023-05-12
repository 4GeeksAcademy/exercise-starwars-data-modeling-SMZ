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
    cast = Column(String(250), nullable=False)
    height = Column(String(30), nullable=False)
    films_id = Column(String(30), nullable=False)
    hair_color = Column(String(30), nullable=False)
    skin_color = Column(String(30), nullable=False)
    eye_color = Column(String(30), nullable=False)
    birth_year = Column(String(30), nullable=False)
    gender = Column(String(30), nullable=False)
    created = Column(String(30), nullable=False)
    edited = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    homeworld_id = Column(Integer, ForeignKey("Planets.id"))
    url = Column(String(250), nullable=False)
    planets_id = relationship("Planets")

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
    cast = Column(String(250), nullable=False)
    characters = Column(String(250), nullable=False)
    planets = Column(String(250), nullable=False)
    starships = Column(String(250), nullable=False)
    vehicles = Column(Integer, ForeignKey("vehicles.id"))
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
    vehicles_id = relationship("Vehicles")

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    model = Column(String(30), nullable=False)
    vehicle_class = Column(String(30), nullable=False)
    manufacturer = Column(String(30), nullable=False)
    cost_in_credits = Column(String(30), nullable=False)
    length = Column(String(30), nullable=False)
    crew = Column(String(30), nullable=False)
    passengers = Column(String(30), nullable=False)
    max_atmosphering_speed = Column(String(30), nullable=False)
    cargo_capacity = Column(String(30), nullable=False)
    consumable = Column(String(30), nullable=False)
    films = Column(String(30), nullable=False)
    pilots = Column(String(30), nullable=False)
    created = Column(String(30), nullable=False)
    edited = Column(String(30), nullable=False)
    url = Column(String(30), nullable=False)
    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    rotation_period = Column(String(30), nullable=False)
    orbital_period = Column(String(30), nullable=False)
    gravity = Column(String(30), nullable=False)
    population = Column(String(30), nullable=False)
    climate = Column(String(30), nullable=False)
    terrain = Column(String(30), nullable=False)
    surface_water = Column(String(30), nullable=False)
    created = Column(String(30), nullable=False)
    edited = Column(String(30), nullable=False)
    url = Column(String(30), nullable=False)

class Cast(Base):
    __tablename__ = 'cast'
    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey("films.id"))
    film = relationship("Films", backref="cast")
    people_id = Column(Integer, ForeignKey("people_id"))
    people = relationship("people")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
