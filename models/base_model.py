#!/usr/bin/python3
"""Defines all common attributes/methods fro other classes."""

import uuid
from datetime import datetime


class BaseModel:
    """Represents the Base Class of the Airbnb Clone class."""
    def __init__(self):
        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__"""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__

    def __str__(self):
        """Returns the pribt/str representattion of BaseModel Instances"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(
            key, type(my_model_json[key]), my_model_json[key]))
