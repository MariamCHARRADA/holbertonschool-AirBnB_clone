#!/usr/bin/python3
"""Basemodel unittesting"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """test cases for the Basemodel class"""

    def test_instance_creation(self):
        """test that an instance is created appropriately"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)

    def test_str_representation(self):
        """test that the string representation is correct"""
        instance = BaseModel()
        str_repr = str(instance)
        self.assertIn("[BaseModel]", str_repr)
        self.assertIn(str(instance.id), str_repr)
        self.assertIn(str(instance.__dict__), str_repr)

    def test_save_method(self):
        """test that the save method updates the updated_at attribute"""
        instance = BaseModel()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(original_updated_at, instance.updated_at)

    def test_multiple_instances(self):
        """Test saving and reloading multiple BaseModel instances"""
        model1 = BaseModel()
        model1.name = "Model 1"
        model1.save()

        model2 = BaseModel()
        model2.name = "Model 2"
        model2.save()

        self.storage.reload()
        reloaded_model1 = self.storage.all()["BaseModel." + model1.id]
        reloaded_model2 = self.storage.all()["BaseModel." + model2.id]

        self.assertEqual(reloaded_model1.name, "Model 1")
        self.assertEqual(reloaded_model2.name, "Model 2")

    def test_to_dict_method(self):
        """test that the to_dict method returns a dictionary"""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIn("__class__", instance_dict)
        self.assertEqual(instance_dict["__class__"], "BaseModel")


if __name__ == "__main__":
    unittest.main()
