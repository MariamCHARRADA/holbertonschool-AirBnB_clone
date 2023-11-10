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
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

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
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        if not arg:
            print("** class name missing **")

        args = arg.split(" ")
        instances = storage.all()
        instance_key = args[0] + "." + args[1]
        
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif instance_key not in instances:
            print("** no instance found **")
        else:
            print(str(instances[instance_key]))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split(" ")
        inst_dict = storage.all()
        if not arg:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 2:
            inst_key = args[0] + "." + args[1]
            if inst_key not in inst_dict:
                print("** no instance found **")
            del inst_dict[args[0] + "." + args[1]]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name
        """
        if arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            for instance in instances.values():
                if instance.__class__.__name__ == arg:
                    print(str(instance))

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = arg.split(" ")
        instance_key = args[0] + "." + args[1]
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif instance_key not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            instance = storage.all()[instance_key]
            setattr(instance, args[2], args[3])
            instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
