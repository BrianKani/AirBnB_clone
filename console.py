#!/usr/bin/python3

"""This module implements a console application for testing and debugging
the AirBnB Clone application."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class for the console application.

    Attributes:
    prompt (str): the prompt issued to solicit input.
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exits the console application when prompted by the user. QUIT"""
        return True

    def do_EOF(self, line):
        """Exits the console application when EOF is reached."""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
