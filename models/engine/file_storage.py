#!/usr/bin/python3
"""file storage"""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """serialization and deserialization"""

    __file_path = "storage_file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, "w") as f:
            dict = {}
            for key, value in self.__objects.items():
                dict[key] = value.to_dict()
            json.dump(dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                dict = json.load(f)
            for key, value in dict.items():
                class_name = key.split(".")[0]
                self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
