import sys

# YOU HAVE TO USE THE TERMINAL !!!!!
# IN THE TERMINAL:
# filename.py ----> runs the python file
# 43_hello.py    ----> runs 43_hello.py
# filename.py firstArgument secondArgument

zero  = sys.argv[0]         # Returns file path
first = sys.argv[1]         # Returns first argument
last  = sys.argv[2]         # Returns second argument

print(f'hiiii {zero} {first} {last}')