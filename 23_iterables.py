#iterables - list, dictionary, tuple, set, string

user = {
    'name': 'Golem',
    'age':   5006,
    'can_swim': False
}

#This is a dictionary case
#With iterables you can use .items(), .values(), .keys()

for item in user:              #Prints all keys in dictionary
    print(item)

print('')

for item in user.keys():       #Prints all keys in dictionary
    print(item)

print('')

for item in user.items():       #Prints keys and values of items in dictionary
    print(item)

print('')

for item in user.values():      #Prints all values of items in dictionary
    print(item)

print('')

for key, value in user.items():  #Prints all keys and values of items in dictionary
    print(key, value)