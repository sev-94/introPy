#Input String in a file
employee_file = open("16_employees.txt", "a")
employee_file.write("\nToby - Human Resources")
employee_file.close()

#Create & Input String in new file
employee_file = open("index.html", "w")
employee_file.write("<p> This is HTML! <p>")
employee_file.close()