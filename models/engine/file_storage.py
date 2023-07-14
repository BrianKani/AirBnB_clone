#!/usr/bin/python3

"""This module"""

from models.base_model import BaseModel
import json


class FileStorage:
    """The storage engine for the AirBnB web app. This allows us to have
    persistance. We are able to convert the dictionary representation
    to a JSON string (serialization) and then recreate our BaseModel from
    a JSON string found in a persistent file (deserialization).
    Class Attributes:
        __file_path (str): path to the JSON file (ex: file.json)
        __objects (dict): empty but will store all objects by
                          <class name>.id (ex: to store a BaseModel object with
                          id=12121212, the key will be BaseModel.12121212)
    Class Methods:
        all: Returns the dictionary __objects.
        new: Sets in __objects the obj with key <obj class name>.id.
        save: Serializes __objects to the JSON file.
        reload: Deserializes the JSON file to __objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects but only if the JSON file
        exists
        """
        try:
            with open(self.__file_path, 'r') as file:
                serialized_objects = json.load(file)

            for key, serialized_obj in serialized_objects.items():
                class_name, obj_id = key.split('.')
                class_ = eval(class_name)
                obj = class_(**serialized_obj)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass
