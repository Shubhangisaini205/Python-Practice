# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
#     - *Input*: [("John", 25), ("Jane", 30)]
#     - *Output*: "John is 25 years old. Jane is 30 years old."


l=[("John", 25), ("Jane", 30)]
res=""
for i in l:
   res = res + f"{i[0]} is {i[1]} years old. "
print(res)  
     