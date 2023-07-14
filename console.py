#!/usr/bin/python3

"""This module implements a console application for testing and debugging
the AirBnB Clone application."""

import cmd
from models.base_model import BaseModel
from models import storage
import models
import inspect


class HBNBCommand(cmd.Cmd):
    """Class for the console application.

    Attributes:
    prompt (str): the prompt issued to solicit input.
    """

    prompt = '(hbnb) '

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it to the JSON file
        and prints the id. Example: $ create BaseModel
        """
        if not line:
            print("** class name missing **")
            return

        class_name = line.split(" ")[0]
        classes = [name for name, obj in globals().items()
                   if inspect.isclass(obj)]

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
        name and id. Example: $ show BaseModel 1234-1234-1234
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objects:
            objects.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on
        the class name. Ex: $ all BaseModel or $ all
        """
        if not line:
            print([str(instance) for instance in storage.all().values()])
        else:
            class_name = line.split()[0]
            try:
                cls = eval(class_name)
                instances = [str(instance) for instance in storage.all(
                ).values() if isinstance(instance, cls)]
                print(instances)
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Example: $ update BaseModel 1234-1234-1234 email 'aibnb@mail.com'"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objects:
            obj = objects[key]
            attr_name = args[2]
            attr_value = args[3]
            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            print("** no instance found **")

    def emptyline(self):
        """When an empty line is executed by the user, do nothing."""
        pass

    def do_quit(self, line):
        """Exits the console application when prompted by the user. QUIT"""
        return True

    def do_EOF(self, line):
        """Exits the console application when EOF is reached."""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
