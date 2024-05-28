#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""

import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInstantiation(unittest.TestCase):
    """Unittests for FileStorage instantiation."""

    def test_FileStorage_instantiation_no_args(self):
        """Tests creating a FileStorage instance with no arguments."""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_args(self):
        """Creates FileStorage instance with an arg raises TypeError."""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_instance(self):
        """Tests that storage is an instance of FileStorage."""
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage(unittest.TestCase):
    """Unittests for the FileStorage class."""

    def setUp(self):
        """Create a temporary test file for saving."""
        self.test_file = "test_file.json"

    def tearDown(self):
        """Remove temporary test file."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_storage_returns_dict(self):
        """Tests if all() returns a dict."""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """Tests if new() adds an object to storage."""
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), models.storage.all())

    def test_new_with_args(self):
        """Tests creating a new object with arguments raises TypeError."""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save_and_reload(self):
        """Tests saving and reloading objects."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()

        # Create a new storage instance to simulate reloading
        new_storage = FileStorage()
        new_storage.reload()

        # Check if reloaded objects are the same as original objects
        self.assertIsNotNone(
            new_storage.all().get("BaseModel.{}".format(obj1.id))
        )
        self.assertIsNotNone(
            new_storage.all().get("BaseModel.{}".format(obj2.id))
        )

    def test_save_to_file(self):
        """Tests saving objects to a file and checks if it's created."""
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))


if __name__ == "__main__":
    unittest.main()
