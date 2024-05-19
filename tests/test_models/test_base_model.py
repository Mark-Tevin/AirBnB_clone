#!/usr/bin/python3
"""Defines unit tests for models/base_model.py

Unittest classes:
    Test_init
    Test_save
    Test_to_dict
    Test_str
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at
        current_updated_at = my_model.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        my_model = BaseModel()
        rdict = my_model.to_dict()

        self.assertIsInstance(rdict, dict)
        self.assertEqual(rdict['__class__'], 'BaseModel')
        self.assertEqual(rdict['id'], my_model.id)
        self.assertEqual(rdict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(rdict['updated_at'], my_model.updated_at.isoformat())

    def test_str(self):
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()
