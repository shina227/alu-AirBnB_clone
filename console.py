#!/usr/bin/python3
"""
Module for console (HBNBCommand)
"""
import cmd
import re
import shlex
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """HBNBCommand console class"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on an empty line input."""
        return False

    def do_EOF(self, arg):
        """EOF (Ctrl+D) to exit the program."""
        print()  # Print a new line for clean exit
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
