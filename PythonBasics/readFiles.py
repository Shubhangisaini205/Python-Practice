# r =>read files
# w => write files and change the file
# a =>append at the end
# r+ => read and write

employee_file = open("employee.txt","r")
print(employee_file.readable())
# print(employee_file.read()) 
# print(employee_file.readline())  # read single line
# print(employee_file.readlines()) # taking each line put them into an array 
# print(employee_file.readlines()[1])  want to access the file of an array

for employee in employee_file.readlines():
    print(employee)

employee_file.close()