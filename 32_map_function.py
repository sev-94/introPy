def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))


# Map Function
# Instead of using the methods above, you can just use the 'map' function
# Map function takes a function and a list as arguments
def multiply_by2(item):
    return item * 2

print(list(map(multiply_by2, [1, 2, 3])))