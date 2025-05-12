#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up method to create an instance for testing"""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test if the instance is properly created"""
        self.assertIsInstance(self.model, BaseModel)

    def test_unique_id(self):
        """Test if each instance has a unique ID"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_created_at_type(self):
        """Test if created_at is of type datetime"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        """Test if updated_at is of type datetime"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_method(self):
        """Test if save() updates the updated_at attribute"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test if to_dict() returns a dictionary with correct keys"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_create_from_dict(self):
        """Test if an instance can be created from a dictionary"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)


if __name__ == '__main__':
    unittest.main()
