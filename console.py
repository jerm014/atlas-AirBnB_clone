#!/usr/bin/python3
"""this file contains code for the console"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["Amenity", 
               "BaseModel", 
               "City",
               "Place",
               "Review",
               "State",
               "User"]
    NO_EXIST = 1
    NO_NAME = 2
    NO_ID = 4
    NO_INSTANCE = 8
    NO_ATTRIBUTE = 16
    NO_VALUE = 32

    @staticmethod
    def show_error(e):
        if e | NO_EXIST
            print("** class doesn't exist **")
        if e | NO_NAME
            print("** class name missing **")
        if e | NO_ID
            print("** instance id missing **")
        if e | NO_INSTANCE
            print("** no instance found **")
        if e | NO_ATTRIBUTE
            print("** attribute name missing **")
        if e | NO_VALUE
            print("** value missing **")

    def do_hbnh(self, line):
        print("hello")


    def do_help(self, arg):
        if arg:
            try:
                f = getattr(self, "show_help_" + arg)
            except AttributeError:
                return
            f()
        else:
            print("Documented commands(type help <topic>):\n"
                  "========================================\n"
                  "create EOF  help  quit")

    def show_help_create(self, line):    
        print("create <class>")
        print()
        print("class can be one of the following:")
        for i in self.classes:
            print (f"  * {i}")
        print()

    def do_create(self, line):
        """create a new instance of an object and save it"""
        if not line:
            self.show_error(NO_NAME)
            return

        cls = line.split()[0]

        if cls not in self.classes:
            self.show_error(NO_EXIST)
            return

        if cls == "Amenity":
            i = Amenity()
        elif cls == "BaseModel":
            i = BaseModel()
        elif cls == "City":
            i = City()
        elif cls == "Place":
            i = Place()
        elif cls == "Review":
            i = Review()
        elif cls == "State":
            i = State()
        elif cls == "User":
            i = User()

        i.save()
        print(i.id)

    def do_show(self, arg):

        args = arg.split()

        if not args:
            self.show_error(NO_NAME)
            return

        cls = arg.split()[0]
        if cls not in self.classes:
            self.show_error(NO_EXIST)
            return

        if len(args) < 2:
            self.show_error(NO_ID)
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            self.show_error(NO_INSTANCE)
            return

        print(storage.all()[key])

    def do_all(self, line):
        list_obj = []
        if line:

            cls = line.split()[0]

            if cls not in self.classes:
                self.show_error(NO_EXIST)
                return

            for key, obj in storage.all().items():
                if key:
                    list_obj.append(str(obj))
        else:
            for obj in storage.all().values():
                list_obj.append(str(obj))
        print(list_obj)

    def do_destroy(self, line):
        args = line.split()

        if not args:
            self.show_error(NO_NAME)
            return

        cls = args[0]

        if cls not in self.classes:
            self.show_error(NO_EXIST)
            return

        if len(args) < 2:
            sef.show_error(NO_ID)
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            self.show_error(NO_INSTANCE)
            return

        del storage.all()[key]
        storage.save()

    def do_update(self, line):
        args = line.split()

        if not args:
            self.show_error(NO_NAME)
            return

        cls = args[0]

        if cls not in self.classes:
            self.show_error(NO_EXIST)
            return

        if len(args) < 2:
            self.show_error(NO_ID)
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            self.show_error(NO_INSTANCE)
            return

        if len(args) < 3:
            self.show_error(NO_ATTRIBUTE)
            return

        if len(args) < 4:
            self.show_error(NO_VALUE)
            return

        obj = storage.all()[key]
        setattr(obj, args[2], args[3])
        obj.save()

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self, line):
        return

    def show_help_quit(self, line):
        print("Quit command to exit the program")

    def show_help_EOF(self, line):
        print("EOF command to exit the program")


if __name__ == "__main__":

    HBNBCommand().cmdloop()
