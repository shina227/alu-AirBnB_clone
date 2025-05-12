#!/usr/bin/python3
"""BaseModel module
Defines a BaseModel class for all other classes in the AirBnB clone project"""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class that defines all common
    attributes and methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    if isinstance(value, str):
                        value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)

            # Set default values if they are missing
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
