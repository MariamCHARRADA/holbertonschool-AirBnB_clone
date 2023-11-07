#!/usr/bin/python3
"""Unit tests for the FileStorage class"""
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """test cases for the FileStorage class"""

    def test_all(self):
        """test that the all method returns a dictionary"""
        storage = FileStorage()
        model = BaseModel()
        model.id = "test_id"
        storage.new(model)
        objects = storage.all()
        self.assertTrue(isinstance(objects, dict))
        self.assertIn("BaseModel.test_id", objects)
        self.assertEqual(objects["BaseModel.test_id"], model)

    def test_new(self):
        """test that the new method adds an object to __objects"""
        storage = FileStorage()
        model = BaseModel()
        model.id = "new_test_id"
        storage.new(model)
        objects = storage.all()
        self.assertIn("BaseModel.new_test_id", objects)
        self.assertEqual(objects["BaseModel.new_test_id"], model)

    def test_save(self):
        """test that the save method serializes __objects to a JSON file"""
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """test that the reload method deserializes JSON file to __objects"""
        self.storage.save()
        self.storage.reload()
        reloaded_objects = self.storage.all()
        self.assertEqual(len(reloaded_objects), 1)
        self.assertEqual(reloaded_objects["BaseModel.test_id"], self.model)


if __name__ == "__main__":
    unittest.main()
