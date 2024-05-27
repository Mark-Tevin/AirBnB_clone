#!/usr/bin/python3
"""
BaseModel module
"""

import uuid
from datetime import datetime, timezone


class BaseModel:
    """
    A base class for other models
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    def save(self) -> None:
        """
        Updates the updated_at attribute with current time
        """
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self) -> dict:
        """
        Converts the instance to a dictionary
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict

    def __str__(self) -> str:
        """
        Returns a string representation of the instance
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


if __name__ == "__main__":
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
            key, type(my_model_json[key]), my_model_json[key])
        )
