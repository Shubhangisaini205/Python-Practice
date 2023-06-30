# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
    # - *Input*: Add "John": 25, Update "John": 26, Delete "John"
    # - *Output*: "{}, {'John': 26}, {}"

def  Add(dictionary, name, age):
    dictionary[name]=age

def  Update(dictionary, name, age2):
    if name in dictionary:
        dictionary[name]=age2

def  Delete(dictionary, name):
    if name in dictionary:
        del dictionary[name]

dict = {}
Add(dict,"Parul",26)    
print(dict)   
Update(dict,"Parul",23)
print(dict)  
Delete(dict,"Parul")
print(dict)  