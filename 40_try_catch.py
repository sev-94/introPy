while True:
    try:
        age = int(input('What is your age?'))
        print(age)
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter a number')
    except TypeError:
        print('please enter a number')
    else:
        print('thank you')
        break

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'please enter numbers {err}') #Print error message

print(sum(1, '2'))