# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."


def Divide(num1,num2):
    if num2 <= 0:
        return "Cannot divide by zero."
    else:
        return num1/num2
    
print(Divide(5,2))   