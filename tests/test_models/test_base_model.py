#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid


class TestBaseModel(unittest.TestCase):

    """Test cases for the BaseModel Class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_init(self):
        """Tests instantiation of BaseModel class."""

        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)
        self.assertIsInstance(my_model, BaseModel)

    def test_init_no_args(self):
        """Tests __init__ with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_init_many_args(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        args = [i for i in range(1000)]
        my_model = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        my_model = BaseModel(*args)

    def test_attributes(self):
        """Tests attribute value for instance of a BaseModel class."""

        attributes = storage.attributes()["BaseModel"]
        o = BaseModel()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

    def test_datetime_created(self):
        """Tests if updated and created date and time are current."""
        date_now = datetime.now()
        my_model = BaseModel()
        diff = my_model.updated_at - my_model.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = my_model.created_at - date_now
        self.asserTrue(abs(diff.total_seconds()) < 0.1)

    def test_user_id(self):
        """Tests for unique user ids."""

        nl = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(nl)), len(nl))

    def test_save(self):
        """Tests the public instance methods save()."""

        my_model = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        my_model.save()
        diff = my_model.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

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
