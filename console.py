#!/usr/bin/python3

import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt= "(hbnb)"
  
        
    def do_create(self, args):
        class_name = args
        if not class_name:
            print("** class name missing **")
            
        else :
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                my_model = HBNBCommand.class_dict[line]()
                my_model.save()
                print(my_model.id)
            
    
    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id."""
        c_name = [0]
        c_id = [2]
        new = args.partition(" ")
        # guard against trailing args
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return
        
        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        
        if not c_id:
            print("** instance id missing **")
            return

        if c_id not in HBNBCommand.classes:
            print("** no instance found **") 
            return
    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")  

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id"""
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return
        
    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Prints all string representation of all instances based or not on the class name"""
        my_dict = storage.all()
        my_list = []
        if len(args) == 0:
            for values in my_dict.values():
                my_list.append(str(values))
            print(my_list)
        else:
            if args not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            else:
                for value in my_dict.values():
                    if value.to_dict()["__class__"] == args:
                        my_list.append(str(value))
                print(my_list)
            
    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_quit(self,command):
        """Method to exit console"""
        exit(0)

    def help_quit(self):
        """program displays help documentation of exit"""
        print("Quit command to exit the program")

    def do_EOF(self,args):
        """program to exit program"""
        print()
        exit(0)

    def help_EOF(self):
        """Display the help documentation of EOF"""
        print("Exits the program without formatting\n")

    def emptyline(self):

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
