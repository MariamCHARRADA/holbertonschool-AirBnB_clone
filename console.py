#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
from models.amenity import Amenity
from models.base_model import BaseModel
import cmd
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from models.user import User
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand that inherits from cmd.Cmd"""

    prompt = "(hbnb) "
    classes = {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def help_quit(self):
        """Help information for the quit command"""
        print("Quit command to exit the program\n")

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        and prints its ID
        """
        args = arg.split(" ")
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            print(new_instance.id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split(" ")

        instances = storage.all()

        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in instances:
            print("** no instance found **")
        else:
            print(str(instances[args[0] + "." + args[1]]))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split(" ")
        inst_dict = storage.all()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            if args[0] + "." + args[1] not in inst_dict:
                print("** no instance found **")
            else:
                del inst_dict[args[0] + "." + args[1]]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name
        """
        args = arg.split(" ")
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            for instance in instances.values():
                print(str(instance))

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = arg.split(" ")
        inst_dict = storage.all()
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in inst_dict:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            instance = inst_dict[args[0] + "." + args[1]]
            setattr(instance, args[2], args[3].replace('"', ""))
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
