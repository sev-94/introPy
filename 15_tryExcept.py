
#Catch invalid inputs from user
try:
    number = int(input("Enter a number"))
    print(number)
except:
    print("Invalid Input")

#Errors included in Library -----------------------
try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")