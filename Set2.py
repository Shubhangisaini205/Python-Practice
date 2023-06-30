
# ### Problem **1: Print the following pattern**

# Write a program to print the following number pattern using a loop.

# ```
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
      print(j,end=" ")
    print()  
 
# ### Problem **2: Display numbers from a list using loop**

# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

# **Given**:

# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```

# **Expected output:**

# ```
# 75
# 150
# 145
# ```

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i > 500:
       break
    if i >150:
       continue
    if i % 5 == 0:
        print(i)


### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

# **Given**:

# ```
# s1 = "Ault"
# s2 = "Kelly"
# ```

# **Expected Output**:

# ```
# AuKellylt
# ```

s1 = "Ault"
s2 = "Kelly"

midIndex = len(s1)//2
s3 = s1[:midIndex]+s2 + s1[midIndex:]
print(s3)


### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# **Given**:

# ```
# str1 = PyNaTive
# ```

# **Expected Output**:

# ```
# yaivePNT
# ```

str1 = "PyNaTive"
lc_str=""
uc_str=""
for char in str1:
   if  char.islower():
      lc_str+=char
   else:
      uc_str+=char  
ans = lc_str+uc_str
print(ans)       
      



# ### Problem **5: Concatenate two lists index-wise**

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# **Given**:

# ```
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# ```

# **Expected output:**
# ```
# ['My', 'name', 'is', 'Kelly']
# ```
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
res = []
for i in range(max(len(list1),len(list2))):
   
    # if i <len(list1):
    #   x = list1[i]  
    # else:
    #     x="" 

    # if i <len(list2):
    #   y = list2[i]  
    # else:
    #   y=""     
    res.append(list1[i]+list2[i])

print(res)



### Problem **6: Concatenate two lists in the following order**

# ```
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# ```

# **Expected output:**

# ```
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# ```


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
output = []
for i in list1:
   for j in list2:
      output.append(i+j) 

print(output)


### Problem **7: Iterate both lists simultaneously**

# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

# **Given**

# ```
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# ```

# **Expected output:**

# ```
# 10 400
# 20 300
# 30 200
# 40 100
# ```

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i in range(min(len(list1),len(list2))):
    print(list1[i], list2[-i - 1])



### Problem **8: Initialize dictionary with default values**

# In Python, we can initialize the keys with the same values.

# **Given**:

# ```
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# ```

# **Expected output:**

# ```
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
# ```    

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# result = {}
# for i in employees:
#    result[i] = defaults

# print(result)
result ={i:defaults for i in employees}
print(result)





### Problem **9: Create a dictionary by extracting the keys from a given dictionary**

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# **Given dictionary**:

# ```
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]
# ```

# **Expected output:**

# ```
# {'name': 'Kelly', 'salary': 8000}
# ```

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

key=["name","salary"]

newDict = {i:sample_dict[i] for i in key}
print(newDict)



### Problem **10: Modify the tuple**

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

# **Given**:

# ```
# tuple1 = (11, [22, 33], 44, 55)
# ```

# **Expected output:**

# ```
# tuple1: (11, [222, 33], 44, 55)
# ```

# tuple1 = (11, [22, 33], 44, 55)
# new_list = list(tuple1)
# print(new_list)
# new_list[1][0]=222
# tuple1 = tuple(new_list)
# print(tuple1)


tuple1 = (11, [22, 33], 44, 55)
for item in tuple1:
    if isinstance(item, list) and len(item) > 0:
        item[0] = 222

print( tuple1)

 # isinstance() is a built-in Python function that is used to check the type of an object. It takes two arguments: the object you want to check and the type you want to check against. The function returns True if the object is an instance of the specified type, and False otherwise.


   

