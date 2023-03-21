#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
            primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True,
            nullable=False)
        )

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary=place_amenity,
            viewonly=False, back_populates="place_amenities")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """Returns the list of Review instances"""
            return [review for review in reviews]

        @property
        def amenities(self):
            """Returns a list of Amenity instances"""
            return [amenity for amenity in amenities]

        @setter.amenities
        def amenities(self, obj):
            """Appends an amenity id to the attribute
            amenity_id
            """
            if type(obj) == "Amenity":
                amenity_ids.append(obj.id)
