#!/usr/bin/python3
"""Console Base module"""
import uuid
import datetime


class BaseModel():
    """BaseModel class the parent of other classes"""

    def __init__(self):
        """initializing the public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    # __str__ method

    def __str__(self):
        """method that return string representation of an instance"""
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"
    # save method

    def save(self):
        """method that updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """method that returns a dictionary containing all
          keys/values of __dict__ of the instance"""
        dic = {}
        for key, value in (self.__dict__.items()):
            if (isinstance(value, datetime.datetime)):
                value = value.isoformat()
            dict[key] = value
        dic['__class__'] = self.__class__.__name__
        return dic
