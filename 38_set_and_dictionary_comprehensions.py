simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items()}
my_dict2 = {k: v**2 for k, v in simple_dict.items()}
my_dict3 = {num:num*2 for num in [1,2,3]}

print(my_dict)
print(my_dict2)
print(my_dict3)