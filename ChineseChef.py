#import Chef file into this file
from Chef import Chef

#import all functions from Chef to ChineseChef
class ChineseChef(Chef):

    #override inherited function
    def make_special_dish(self):
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes friend rice")