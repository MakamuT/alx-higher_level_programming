#!/usr/bin/python3
"""Defines a base class"""
import json
import csv
import turtle


class base:
    """ Base model
    This represents the "base' for all classes in this project

    Private Class
    Attributes:
            __nb__object(int):
    Number of instantiated bases
    """
    __nb__objects = 0

    def __init__(self, id=None):
        """Initialize a new base
          Args:
            id(int): the identity of  the new base
            """
            if id is not None:
                self.id = id
            else:
                Base.__nb_objects += 1
                    self.id = Base.__nb_objects

                    @staticmethod 
                    def to_json_string(list_dictionaries):
                        """Return the JSON serialization of a list of dictionaries
                        Args:
                        list_dictionaries(lists):
                        list of dictionaries
                        """
                        if list_dictionaries is None or list_dictionaries == []:
                            return "[]"
                        return json.dumps(list_dictionaries)
                    
                    @classmethod 
                    def save_to_file(cls, list_obj):
                        """write JSON serialization of a list of objects to a file
                        Args:
                        list_obj(list):
                        list of inherited base instances
                        """
                        filename = cls.__name__ + ".json"
                        with open(filename, "w") as jsonfile:
                            if list_obj is None:
                                jsonfile.write("[]")
                            else:
                                list_dictionaries = [o.to_dictionary() for o in list_obj)]
                                jsonfile.write(Base. to_json_string(list_dictionaries)
                                        @staticmethod
                                        def from_json_string(json_string):
                                        """
                                        Returns a list of Python dictionaries from a JSON string
                                        representation.

                                        Args:
                                        json_string (str): A string representing a list of dictionaries
                                        in JSON format.
                                        Returns:
                                        A list of dictionaries. If the input string is None or empty,
                                        returns an empty list.
                                        """
                                        if json_string is None or json_string == '[]':
                                        return []
                                        return json.loads(json_string)
                                        @classmethod
                                        def create(cls, **dictionary):
                                        """Returns an instance with all attributes already set."""
                                        if dictionary and dictionary != {}:
                                        if cls.__name__ == "Rectangle":
                                        dummy = cls(1, 1)
                                        elif cls.__name__ == "Square":
                                            dummy = cls(1)
                                            dummy.update(**dictionary)
                                        return dummy
                                        @classmethod
                                        def load_from_file(cls):
                                        """Returns a list of instances from a JSON file."""
                                        filename = cls.__name__ + ".json"
                                        try:
                                            with open(filename, "r") as file:
                                            json_string = file.read()
                                            except FileNotFoundError:
                                            return []
                                            object_list = cls.from_json_string(json_string)
                                            instance_list = [cls.create(**obj_dict) for obj_dict in object_list]
                                            return instance_list
