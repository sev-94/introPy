def say_hi():
    print("Hello User")
say_hi()

def say_hi(name):
    print("Hello User" + name)
say_hi(" Mike")
say_hi(" Steve")

def say_hi(name, age):
    print("Hello User" + name + " " + age)
say_hi(" Mike", "22")

def say_hi(name, age):
    print("Hello User" + name + " " + str(age))
say_hi(" Mike", 18)