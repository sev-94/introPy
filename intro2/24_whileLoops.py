i = 0

#When using a while, if you dont have a break it will keep running through the 'else'
while i < 50:
    print(i)
    i += 1
    break
else:
    print('done')

#If there is no 'break' in the while, the 'else' statement will also run
while i < 50:
    print(i)
    i += 1
else:
    print('done')

#User input for break ------------------------------------------------------
while True:
    response = input('say something: ')
    if (response == 'bye'):
        break