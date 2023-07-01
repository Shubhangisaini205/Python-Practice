# List

luckyNumbers = [1,2,3,4]
friends=["shubh", "rutvik","Aditya","sachi","Arti","Aditya"]
# friends.extend(luckyNumbers) # it will add luckunumber in the list friend
friends.append("Parul")  # add at the end
friends.insert(1,"Kayle")
friends.remove("shubh")
# friends.clear()  # clear all the elements
friends.pop()  # remove last element of  list

# print(friends.index("Aditya")) # it give the index of particular elemeny
# print(friends.count("Aditya"))  count the frequency
# friends.sort()  it will sort the list 

luckyNumbers.reverse()
friends2 = friends.copy()
# print(friends2)


# Tuple; tuples is immmutable we can not change the tuple

coordinates =(2,4)

print(coordinates[0])




