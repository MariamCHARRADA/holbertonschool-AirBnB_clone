#!/usr/bin/python3
"""User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __str__(self):
        """method that returns the string representation of an instance"""
        return f"[{User.__name__}] ({self.id}) {self.__dict__}"
