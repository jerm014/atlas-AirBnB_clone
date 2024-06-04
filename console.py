#!/usr/bin/python3
"""this file contains code for the console"""

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass

    def do_help(self, arg):
        cmd.Cmd.do_help(self, arg)

    def default(self, line):
        if line == '':
            return
        else:
            print(f"Invalid command: {line}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
