#!/usr/bin/python3
"""
Unit tests for BaseModel
"""

from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """

    def test_init(self):
        """
        Test initialization of BaseModel
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_save(self):
        """
        Test the save method of BaseModel
        """
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at
        my_model.save()
        current_updated_at = my_model.updated_at

        self.assertNotEqual(initial_updated_at, current_updated_at)
        self.assertTrue(current_updated_at > initial_updated_at)  # type:ignore

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict["id"], my_model.id)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(my_model_dict["created_at"],
                         my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"],
                         my_model.updated_at.isoformat())
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        """
        Test the __str__ method of BaseModel
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == '__main__':
    unittest.main()
