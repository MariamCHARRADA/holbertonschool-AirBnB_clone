#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand that inherits from cmd.Cmd"""

    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
