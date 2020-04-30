#print text from file
employee_file = open("16_employees.txt")
print(employee_file.read())
employee_file.close()


#print one line of text from file - in order
employee_file = open("16_employees.txt")
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
employee_file.close()

#print text from file in a single line
employee_file = open("16_employees.txt")
print(employee_file.readlines())
employee_file.close()

#print specific line from file
employee_file = open("16_employees.txt")
print(employee_file.readlines()[2])
employee_file.close()

#print text from file
employee_file = open("16_employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()