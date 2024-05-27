#!/usr/bin/python3
"""
BaseModel module
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    A base class for other models
    """
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel
        Args:
            - *args: Not used here
            - **kwargs: dictionary of key-values arguments
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k in ['created_at', 'updated_at'] and isinstance(v, str):
                    v = datetime.strptime(v, self.TIME_FORMAT)
                setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self) -> None:
        """
        Updates the updated_at attribute with current time
        """
        self.updated_at = datetime.utcnow()

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
