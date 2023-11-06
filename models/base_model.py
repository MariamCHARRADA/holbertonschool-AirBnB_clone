#!/usr/bin/python3
"""Console Base module"""
import uuid
import datetime


class BaseModel:
    """BaseModel class the parent of other classes"""

    def __init__(self, *args, **kwargs):
        """initializing the public instance attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"
                        )
                    self.to_dict[key] = value

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
        for key, value in self.__dict__.items():
            if isinstance(value, datetime.datetime):
                value = value.isoformat()
            dict[key] = value
        dic["__class__"] = self.__class__.__name__
        return dic
