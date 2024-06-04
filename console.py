#!/usr/bin/python3
"""this file contains code for the console"""

import cmd
from models.base_model import Base_Model
import json

file_path = "file.json"

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quit cmd to leave program"""
        return True

    def do_EOF(self, arg):
        """EOF cmd to leave program"""
        return True

    def emptyline(self):
        """do nothing on empty input"""
        pass

    def do_create(self, arg):
        """creates new BaseModel instance, saves and prints id"""
        if not arg:
            print("** missing class name **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_help(self, arg):
        """help information"""
        cmd.Cmd.do_help(self, arg)

    def default(self, line):
        """handles invalid command"""
        if line == '':
            return
        else:
            print(f"Invalid command: {line}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
