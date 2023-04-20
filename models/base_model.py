#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from os import getenv

Base = declarative_base()
storage_type = getenv('HBNB_TYPE_STORAGE')


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif k != '__class__':
                    setattr(self, k, v)
            if storage_type == 'db':
                if not hasattr(kwargs, 'id'):
                    setattr(self, 'id', str(uuid.uuid4()))
                if not hasattr(kwargs, 'created_at'):
                    setattr(self, 'created_at', datetime.now())
                if not hasattr(kwargs, 'updated_at'):
                    setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """Returns a string representation of the instance"""
        dictionary = self.__dict__.copy()
        dictionary.pop("_sa_instance_state", None)
        return '[{}] ({}) {}'.format(
                                     self.__class__.__name__,
                                     self.id,
                                     dictionary)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = str(type(self).__name__)
        for key in dictionary:
            if isinstance(dictionary[key], datetime):
                dictionary[key] = dictionary[key].isoformat()

        if dictionary['_sa_instance_state']:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage

        storage.delete(self)
