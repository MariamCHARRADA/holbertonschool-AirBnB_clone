#!/usr/bin/python3
"""Console Base module"""
import uuid
import datetime


class BaseModel():
    """BaseModel class"""

    def __init__(self):
        """public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    # __str__ method

    def __str__(self):
        """__str__ method"""
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"
    # save method

    def save(self):
        """save method"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """to_dict"""
        dic = {}
        for key, value in (self.__dict__.items()):
            if (isinstance(value, datetime.datetime)):
                value = value.isoformat()
            dict[key] = value
        dic['__class__'] = self.__class__.__name__
        return dic
