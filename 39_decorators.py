#Decorators are used when a function is used as an argument for another function
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func

#This is a 'decorator'
#Decorators are declared with a '@' in front of them
#Decorators add extra functionality to existing functions
@my_decorator
def hello(greeting):
    print(greeting)

hello('hiii')