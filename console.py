#!/usr/bin/python3

"""This module implements a console application for testing and debugging
the AirBnB Clone application."""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for the console application.

    Attributes:
    prompt (str): the prompt issued to solicit input.
    """

    prompt = '(hbnb) '

    def do_create(self, line, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file
        and prints the id. Example: $ create BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        new_instance = storage.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    

    def do_quit(self, line):
        """Exits the console application when prompted by the user. QUIT"""
        return True

    def do_EOF(self, line):
        """Exits the console application when EOF is reached."""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
