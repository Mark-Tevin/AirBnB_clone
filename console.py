#!/usr/bin/python3
"""
Module for the entry point of the command interpreter.
"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class for the command interpreter.

    Args:
        cmd (cmd.Cmd): The base class for building command line interfaces.
    """

    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def emptyline(self):
        """Does nothing upon receiving an empty line."""
        pass

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
        EOF signal to exit the program.
        """
        print()
        return True

    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file.

        Usage: create <class_name>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance.

        Usage: show <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.

        Usage: destroy <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances.

        Usage: all [class_name]
        """
        commands = shlex.split(arg)
        objects = storage.all()

        if len(commands) == 0:
            for obj in objects.values():
                print(str(obj))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, obj in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(obj))

    def do_update(self, arg):
        """
        Updates an instance by adding or updating an attribute.

        Usage: update <class_name> <id> <attribute_name> <attribute_value>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        elif len(commands) < 3:
            print("** attribute name missing **")
        elif len(commands) < 4:
            print("** value missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            else:
                obj = objects[key]
                attr_name = commands[2]
                attr_value = commands[3]

                try:
                    # Try to convert attribute value to its actual type
                    attr_value = eval(attr_value, {"__builtins__": {}})
                except (NameError, SyntaxError):
                    # Handle cases where eval fails
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
