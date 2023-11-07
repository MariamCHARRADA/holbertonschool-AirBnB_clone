#!/usr/bin/python3
import json
import os


class FileStorage:
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
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
