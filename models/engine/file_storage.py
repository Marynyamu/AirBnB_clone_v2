#!/usr/bin/python3
"""
Serializes instances to a JSON file and
deserializes JSON file to instances.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

"""class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}
 Filestorage == type(self)"""


class FileStorage:
    """The file storage engine class, that is;
    A class that serialize and deserialize instances to a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""

        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""

        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        new_dict = []
        for obj in type(self).__objects.values():
            new_dict.append(obj.to_dict())
            # for key, obj in type(self).__objects.items():
            #    new_dict[key] = obj.to_dict()
        with open(type(self).__file_path, "w", encoding='utf-8') as file:
            json.dump(new_dict, file)


    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        try:
            with open(FileStorage.__file_path) as file:
                dict_from_json = load(file)
                for obj in dict_from_json.values():
                    self.new(eval(obj['__class__'])(**obj))
        except Exception:
            return
