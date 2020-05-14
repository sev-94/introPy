import re                        # Import Regular Expressing 're'

string = 'search this inside of this text please!'

a = re.search('this', string)    # Set search to look for a string 'this'

print(a)                         # Information about the string
print(a.span())                  # Start and End locations of the string
print(a.start())                 # Location of the start of the string
print(a.end())                   # Location of the end of the string
print(a.group())                 # Print group of chars matching string

pattern = re.compile('this')     # Set a pattern to search for
a2 = pattern.search(string)      # Finds first instance of pattern
a3 = pattern.findall(string)     # Finds all instances of the pattern
a4 = pattern.fullmatch('this')   # Checks if the parameter exactly matches pattern
a5 = pattern.match(string)       # Checks if the parameter exactly matches pattern up to a point
print(a2)
print(a3)
print(a4)
print(a5)