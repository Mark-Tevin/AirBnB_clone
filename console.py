#!/usr/bin/python3
"""
Module for the entry point of the command interpreter.
"""

import cmd
import shlex
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class for the command interpreter.

    Args:
        cmd (cmd.Cmd): The base class for building command line interfaces.
    """

    prompt = "(hbnb)"
    valid_classes = [
        "BaseModel", "User", "Amenity",
        "Place", "Review", "State", "City"
    ]

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
        """EOF signal to exit the program."""
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
            new_instance = eval(f"{commands[0]}()")
            storage.save()
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
        objects = storage.all()
        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def default(self, arg):
        """Default behavior of the cmd for invalid syntax."""
        arg_list = arg.split('.')
        incoming_class = arg_list[0]

        command = arg_list[1].split('(')
        incoming_method = command[0]

        method_dict = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
            'count': self.do_count
        }

        if incoming_method in method_dict.keys():
            return method_dict[incoming_method]("{} {}".format(incoming_class, ''))

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """Counts and retrieves the number of instances of a class."""
        objects = storage.all()
        commands = shlex.split(arg)

        if arg:
            incoming_class = commands[0]

        count = 0

        if commands:
            if incoming_class in self.valid_classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == incoming_class:
                        count += 1
                print(count)
            else:
                print("** Invalid class name **")
        else:
            print("** class name missing **")

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
        elif commands[1] not in storage.all():
            print("** no instance found **")
        elif len(commands) < 3:
            print("** attribute name missing **")
        elif len(commands) < 4:
            print("** value missing **")
        else:
            obj = storage.all()[commands[1]]
            attr_name = commands[2]
            attr_value = commands[3]

            try:
                attr_value = eval(attr_value)
            except Exception:
                pass
            setattr(obj, attr_name, attr_value)
            obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
