#!/usr/bin/python3
"""Console Base module"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """BaseModel class: the parent of other classes"""

    def __init__(self, *args, **kwargs):
        """initializing the public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """method that returns the string representation of an instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """method that updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """method that returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        dic = self.__dict__.copy()
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dic[key] = value.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
