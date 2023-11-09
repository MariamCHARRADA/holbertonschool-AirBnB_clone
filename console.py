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


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand that inherits from cmd.Cmd"""

    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}

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
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            instance = eval(arg)()
            if instance:
                print("{}".format(instance))
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            instance = eval(arg)()
            if instance:
                del instance
                storage.save()
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

        def all(self, arg):
            """Prints all string representation of all
            instances based or not on the class name
            """
            if not arg:
                print("** class doesn't exist **")
                return
            else:
                instances = eval(arg)()
                for instance in instances:
                    print("{}".format(instance))
                    
        def do_update(self, arg):
            """Updates an instance based on the class name
            and id by adding or updating attribute
            """
            if not arg:
                print("** class name missing **")
                return
            args = arg.split(" ")
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance = args[0] + "." + args[1]
            if instance not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
