#!/usr/bin/python3
"""
Module for the entry point of the command interpreter.
"""

import cmd
import json


class HBNBCommand(cmd.Cmd):
    """
    Class for the command interpreter.

    Args:
        cmd (cmd.Cmd): The base class for building command line interfaces.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Args:
            arg (str): The command argument.
        """
        return True

    def help_quit(self):
        """
        Prints the help documentation for the quit command.
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Handles End Of File character to exit the program.

        Args:
            arg (str): The command argument.
        """
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
