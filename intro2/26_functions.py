# --- 1 - How to declare a function
# --- 2 - How to declare a function with parameters + How to use Positional & Keyword Arguments
# --- 3 - How to declare a function with 'default' parameters
# --- 4 - Return Statements
# --- 5 - Docstrings
# --- 6 - *args & **kwargs

# ---1--- This is how you define a function in Python ------------------------------------------------------------------
def say_hello():
    print('hellooooo')

say_hello()  # This is how you call a function in Python


# ---2--- Function with  'positional' and 'keyword' parameters ---------------------------------------------------------
def say_hello(name, emoji):
    print(f'hellooooo {name} {emoji}')

say_hello('Andrei', "\U0001f600")  # ---- POSITIONAL ARGUMENT

say_hello('Nick', "\N{grinning face}")  # ---- POSITIONAL ARGUMENT

say_hello(emoji="\U0001F606", name='Sev')  # ---- KEYWORD ARGUMENT


# ---3--- Function with 'default' parameters ---------------------------------------------------------------------------
def say_hello(name='Darth Vader', emoji="\U0001F923"):  # ---- SETTING DEFAULT ARGUMENT
    print(f'hellooooo {name}{emoji}')

say_hello()


# ---4--- Function with Return Statement -------------------------------------------------------------------------------
def add(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)
    return 5                           # This line will not execute, because the function will exit at the first return
    print('hello')                     # This line will not execute, because the function will exit at the first return

total = add(10, 20)
print(total)

# ---5--- Function with Docstrings -------------------------------------------------------------------------------------
def test(a):
    '''
    Info: This function tests and prints param a
    '''
    print(a)

print(test)            #Prints out 'function test at <HEX ADDRESS>
print(test.__doc__)    #Prints out full docstrings info inputted above

#RULE FOR PARAMETERS AND ARGUMENTS - They must be defined in a specific order ------------------------------------------
#RULE: The order of these must be ( params, *args, default params, **kwargs) -------------------------------------------
# ---6a--- By using '*args' you do not need to define a specific number of arguments ------------------------------------
def super_func(*args):
    print(args)
    return sum(args)

print(super_func(1,2,3,4,5))
print(super_func(1,2,3,4,5,6,7,8,9))

# ---6b--- By using '*kwargs' you do not need to define a specific number of keyword arguments
def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))

# ---6c--- Declaring params, *args, default params, **kwargs all in the same function
def super_func(name, *args, i='hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))