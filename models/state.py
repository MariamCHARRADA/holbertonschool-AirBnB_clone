#!/usr/bin/python3
"""Class of State"""
from models.base_model import BaseModel


class state(BaseModel):
    """State Class that inherit from BaseModel Class"""
    name = ""

    def __str__(self):
        """method that return string repesentation of an instance"""
        return f"[{state.__name__}] ({self.id}) {self.__dict__}"
