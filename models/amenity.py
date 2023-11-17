#!/usr/bin/python3
"""Class of Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class that inherit from BaseModel Class"""

    name = ""

    def __str__(self):
        """method that return string representation of an instance"""
        return f"[{Amenity.__name__}] ({self.id}) {self.__dict__}"
