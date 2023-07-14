#!/usr/bin/python3

"""This module includes the base class for all other classes with
common public instance attributes and methods.
"""

from datetime import datetime
import models
import uuid


class BaseModel:
    """Base class that defines all common attributes/methods for
    other classes.

    Class Methods:
        __init__: Instantiation of attributes.
            save: Updates the public instance attribute updated_at with the
                  current datetime.
         to_dict: Returns a dictionary containing all keys/values of __dict__
                  of the instance.
         __str__: String representation of the base class attributes.
    """

    def __init__(self, *args, **kwargs):
        """Instantiation of attributes
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        If kwargs is not empty:
            - Each key of the directory is an attribute name.
            - Each value of the dictionary is the value of the attribute name.
            - The 'created_at' and 'updated_at' attributes are converted to
              datetime objects.
        Otherwise, if kwargs is empty:
            - 'id' and 'created_at are generated for a new instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """Updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__
        of the instance.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict

    def __str__(self):
        """String representation of base class attributes"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
