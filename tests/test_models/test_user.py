#!/usr/bin/python3
"""
Unit tests for the User class.
"""

import os
import unittest
import models
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def setUp(self):
        """
        Sets up a temporary file for storage before each test.
        """
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        """
        Removes the temporary file after each test.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attributes(self):
        """
        Tests the default attributes of a User instance.
        """
        test_user = User()
        self.assertEqual(test_user.email, "")
        self.assertEqual(test_user.password, "")
        self.assertEqual(test_user.first_name, "")
        self.assertEqual(test_user.last_name, "")

    def test_user_inherits_from_basemodel(self):
        """
        Tests if the User class inherits from BaseModel.
        """
        test_user = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str_representation(self):
        """
        Tests the string representation of a User instance.
        """
        test_user = User()
        test_user.email = "tevin@example.com"
        test_user.first_name = "Tevin"
        test_user.last_name = "John"
        test_user.password = "password123"
        user_str = str(test_user)
        self.assertIn("User", user_str)
        self.assertIn("tevin@example.com", user_str)
        self.assertIn("Tevin", user_str)
        self.assertIn("John", user_str)

    def test_user_to_dict(self):
        """
        Tests the dictionary representation of a User instance.
        """
        test_user = User()
        test_user.email = "tevin@example.com"
        test_user.first_name = "Tevin"
        test_user.last_name = "John"
        test_user.save()
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "tevin@example.com")
        self.assertEqual(user_dict['first_name'], "Tevin")
        self.assertEqual(user_dict['last_name'], "John")

    def test_user_instance_creation(self):
        """
        Tests creating a User instance with specific attributes.
        """
        test_user = User(email="tevin@example.com", password="password123",
                         first_name="Tevin", last_name="John")
        self.assertEqual(test_user.email, "tevin@example.com")
        self.assertEqual(test_user.password, "password123")
        self.assertEqual(test_user.first_name, "Tevin")
        self.assertEqual(test_user.last_name, "John")

    def test_user_instance_to_dict(self):
        """
        Tests dictionary conversion of User instance with attributes.
        """
        test_user = User(email="tevin@example.com", password="password123",
                         first_name="Tevin", last_name="John")
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "tevin@example.com")
        self.assertEqual(user_dict['password'], "password123")
        self.assertEqual(user_dict['first_name'], "Tevin")
        self.assertEqual(user_dict['last_name'], "John")

    def test_user_id_generation(self):
        """
        Tests that each User instance has a unique ID.
        """
        test_user1 = User()
        test_user2 = User()
        self.assertNotEqual(test_user1.id, test_user2.id)


if __name__ == '__main__':
    unittest.main()
