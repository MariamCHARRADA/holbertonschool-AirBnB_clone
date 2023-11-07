#!/usr/bin/python3
"""Class of Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class that inherit from BAseModel Class"""
    place_id = ""
    user_id = ""
    text = ""

    def __str__(self):
        """method that return string repesentation of an instance"""
        return f"[{Review.__name__}] ({self.id}) {self.__dict__}"
