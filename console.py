#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
<<<<<<< HEAD
from models import storage
=======
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
>>>>>>> a49439a17d54cf8cd9f41afc672a7cab505e83c3


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand that inherits from cmd.Cmd"""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
