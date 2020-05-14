# This file is originally on the Desktop
# The path to this file is C:\Users\sevag\OneDrive\Desktop\test.txt
# To run this file you must use a terminal
# cd \Users\sevag\OneDrive\Desktop\       changes directory to the dekstop
# 48_script.py                               runs the file
my_file = open('../../OneDrive/Desktop/test.txt')  # Access the file

print(my_file.read())       # Print the whole file
my_file.seek(0)             # Move the cursor
print(my_file.read())       # Print the whole file
my_file.seek(0)             # Move the cursor
print(my_file.read())       # Print the whole file
my_file.seek(0)             # Move the cursor

print(my_file.readline())   # Print one line, new line
print(my_file.readline())   # Print next line, new line
print(my_file.readline())   # Print next line, new line

my_file.close()
