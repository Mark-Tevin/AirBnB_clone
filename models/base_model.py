#!/usr/bin/python3
"""Defines all common attributes/methods fro other classes."""

import uuid
from datetime import datetime


class BaseModel:
    """Represents the Base Class of the Airbnb Clone class."""
    def __init__(self, *args, **kwargs):
        """Instatntiation of the BaseModel
        Args:
            *args (any): Not used
            **kwargs (dict): key/value pairs to attributes
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
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

        return rdict

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
    for key, value in my_model_json.items():
        print("\t{}: ({}) - {}".format(
            key, type(value), value
        ))
