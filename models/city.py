#!/usr/bin/python3
"""Class of City"""
from models.base_model import BaseModel
class city(BaseModel):
    """City Class that inherit from BaseModel Class"""
    state_id = ""
    name = ""
    def __str__(self):
        """method that return string repersentation of an instance"""
        return f"[{city.__name__}] ({self.id}) {self.__dict__}"
    
