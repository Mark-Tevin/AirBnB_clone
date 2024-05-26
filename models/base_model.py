#!/usr/bin/python3
"""
The uuid module is used for creation of unique ids
Date and time module helps us work with time
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    def __init__(self):
        """Initializes a new instance of BaseModel."""
        self.id = str(uuid4())

        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Helps save every created instance"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Helps convert objects to dictionary"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        return obj_dict

    def __str__(self):
        """Returns the string rep of instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


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
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
