#!/usr/bin/python3
"""Class if User"""
from models.base_model import BaseModel
class User(BaseModel):
    """User Class that inherits from BaseMidel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __str__(self):
        """method that return string repesentation of an instance"""
        return f"[{User.__name__}] ({self.id}) {self.__dict__}"
