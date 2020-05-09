#Using Range ----------------------------------
for _ in range(0, 10):
    print(_)

for _ in range(0, 10, 2):
    print(_)

for _ in range(2):
    print(list(range(10)))

#Using Enumerate --------------------------------
for i,char in enumerate('Hello'):
    print(i, char)

print('')

for i,char in enumerate([1,2,3]):
    print(i, char)

print('')

for i,char in enumerate(list(range(100))):
    print(i,char)
    if char == 50:
        print(f'index of 50 is: {i}')
