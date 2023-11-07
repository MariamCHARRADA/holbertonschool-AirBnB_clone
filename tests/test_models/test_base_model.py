#!/usr/bin/python3
"""Basemodel unittesting"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """test cases for the basemodel class"""

    def test_instance_creation(self):
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)

    def test_str_representation(self):
        instance = BaseModel()
        str_repr = str(instance)
        self.assertIn("[BaseModel]", str_repr)
        self.assertIn(str(instance.id), str_repr)
        self.assertIn(str(instance.__dict__), str_repr)

    def test_save_method(self):
        instance = BaseModel()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(original_updated_at, instance.updated_at)

    def test_to_dict(self):
        """test that the to_dict method returns a dictionary"""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIn("__class__", instance_dict)
        self.assertEqual(instance_dict["__class__"], "BaseModel")


if __name__ == "__main__":
    unittest.main()
