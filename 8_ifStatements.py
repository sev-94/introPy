is_male = True
is_tall = True

if is_male:
    print("You are male")
else:
    print("You are female")

if is_male or is_tall:
    print("You are male or tall")
else:
    print("You are not male or you are not tall")

if is_male and is_tall:
    print("You are male and tall")
else:
    print("You are not male and you are not tall")

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif is_male and not (is_tall):
    print("You are female and tall")
else:
    print("You are not male or you are not tall or both")

#calculator----------------------------------------------------------

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op =="+":
    print(num1 + num2)
elif op =="-":
    print(num1 - num2)
elif op =="/":
    print(num1 / num2)
elif op =="*":
    print(num1 * num2)
else:
    print("Invalid operator")