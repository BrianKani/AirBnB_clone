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

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it to the JSON file
        and prints the id. Example: $ create BaseModel"""
        if not line:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        new_instance = storage.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
        name and id. Example: $ show BaseModel 1234-1234-1234"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not_in storage.classes:
            print("** class doesn't exist **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        instance = storage.all()[key]
        print(instance)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not_in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not on
        the class name. Ex: $ all BaseModel or $ all"""
        if not line:
            instance_list = []
            for instance in storage.all().values():
                instance_list.append(str(instance))
            print(instance_list)
        else:
            class_name = line.split()[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
                return
            instance_list = []
            for key, instance in storage.all().items():
                if key.split('.')[0] == class_name:
                    instance_list.append(str(instance))
            print(instance_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]
        instance = storage.all()[key]
        attribute_type = type(getattr(
            instance, attribute_name, None
        ))
        try:
            setattr(instance, attribute_name, attribute_type(attribute_value))
        except ValueError:
            print("** value must be of type{} **".format(
                attribute_type.__name__
            ))
            return

        instance.save()

    def do_quit(self, line):
        """Exits the console application when prompted by the user. QUIT"""
        return True

    def do_EOF(self, line):
        """Exits the console application when EOF is reached."""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
