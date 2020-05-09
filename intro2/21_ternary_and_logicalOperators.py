

#Ternary Operator -------- Good for True/False statements
is_friend = True
can_message = "message allowed" if is_friend else "not allowed"

print(can_message)

#Logical Operators   --- 'and' 'or' & 'not' are keywords you can use

is_friend = True
is_user = False

if is_friend and is_user:
    print('ok1')

if is_friend or is_user:
    print('ok2')

if True and is_user:
    print('ok3')

if True or is_user:
    print('ok4')

if False and is_user:
    print('ok5')

if False or is_user:
    print('ok6')

# 'is' vs '=='  -----  'is' checks the memory location that the variable is stored in
print(True == 1)
print(10 == 10.0)

print(True is 1)
print(10 is 10.0)