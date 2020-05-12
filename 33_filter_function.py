def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))

# Filter Function
# Instead of using the methods above, you can just use the 'filter' function
# Filter function takes a function and a list as arguments

my_list = [1,2,3]

def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))
print(my_list)