#Long way of storing string in a list of chars
my_list = []
for char in 'hello':
    my_list.append(char)

#List Comprehensions
my_list2 = [char for char in 'hello']     #Faster method of storing string in list of chars
my_list3 = [num for num in range(0, 100)] #Create a list of ints until 100 and store in list
my_list4 = [num*2 for num in range(0,100)]
my_list5 = [num**2 for num in range(0,100) if num % 2 == 0]

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)
print(my_list5)