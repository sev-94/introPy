# This file is originally on the Desktop
# The path to this file is C:\Users\sevag\OneDrive\Desktop\test2.txt
# To run this file you must use a terminal
# cd \Users\sevag\OneDrive\Desktop\       changes directory to the dekstop
# 48_script2.py                              runs the file

# mode = 'r'  - to read         : Cannot add any new text or overwrite old text
# mode = 'w'  - to write        : Clears file and overwrites with with new text
# mode = 'r+' - to read & write : Sets cursor at 0 and overwrites existing data, only where needed
# mode = 'a'  - append          : Adds text to the end of existing text

try:
    with open('../../OneDrive/Desktop/test2.txt', mode='a') as my_file:
        text2 = my_file.write(':)')
        print(text2)
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err

