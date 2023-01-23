import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido1 = Column(String(250), nullable=False)
    apellido2 = Column(String(250))
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    planet_fav = relationship(Planet_fav)
    character_fav = relationship(Character_fav)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    character_height = Column(String(250))

class Planet(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    planet_population = Column(Integer)

class Planet_fav(Base):
    __tablename__ = 'planet_fav'
    id = Column(Integer, primary_key = True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planet_id = Column(Integer, ForeignKey('planet_id'))
    usuario = relationship(Usuario)

class Character_fav(Base):
    __tablename__ = 'character_fav'
    id = Column(Integer, primary_key = True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    character_id = Column(Integer, ForeignKey('character_id'))
    usuario = relationship(Usuario)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
