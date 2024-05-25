#!/usr/bin/python3
"""Defines File Storage Class"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Reprsents an abstracted storage engine.
    Attributes:
        __file_path (str): The name of file to save objects to.
        __objects (dict): Dictionary of instantiated objects

    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_class_name = obj.__class__.__name__

        key = "{}.{}".format(obj_class_name, obj.id)

        FileStorage.__objects[key] = obj

    def all(self):
        """Return the dictionary __objects, retreives all objects stored"""
        return FileStorage.__objects

    def save(self):
        """Serialize __objects to JSON format __file_path."""
    all_objs = FileStorage.__objects
    obj_dict = {}

    for obj in all_objs.keys():
        obj_dict[obj] = all_objs[obj].to_dict()

    with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
        json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects, if it exists."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8")as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)

                        instance = cls(**values)

                        FileStorage.__objects[key] = instance

                except FileNotFoundError:
                    return
