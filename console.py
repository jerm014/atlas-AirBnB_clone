#!/usr/bin/python3
"""this file contains code for the console"""

import cmd

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
