#1
print("Hello, World!")


# 2 Data type  Play
#integer
number  = 10
print("Type of number:", type(number), ", value:",number)

#Float
float_number = 3.24
print("Type of float_number:", type(float_number), ", value:",float_number)

#String
name = "Shubhangi Saini"
print("Type of name:", type(name), ",. value:",name)


# Boolean
isTrue =True
print("Type of isTrue:", type(isTrue), ", value:",isTrue)

#List
my_list = [1,2,4,6,7]
print("Type of my_list:", type(my_list), ", value:",my_list)

# Tuple;
my_Tuple = (3,4,5,6,7)
print("Type of my_tuple:", type(my_Tuple), ", value:",my_Tuple)

# Dictionary;
my_Dict = {"name":"Shubh","age":25}
print("Type of my_Dict:", type(my_Dict), ", value:",my_Dict)

# set
my_set = {1, 2, 3, 4, 5}
print("Type of my_set:", type(my_set), ", value:", my_set)


# 3 List Operations

new_List = list(range(1,10))
print("List  is:", new_List)

# Add a number
new_List.append(20)
print("List after adding 20:", new_List)

# Remove a number
new_List.remove(3)
print("List after removing 3:", new_List)

# Sort the list
new_List.sort()
print("Sorted list:", new_List)


# 4. sum and Average;

numbers = [ 10,20,30,40]
total = sum(numbers)
average = total/len(numbers)

print("Sum:", total)
print("Average:", average)


# 5: String Reversal

def String_Rev(str):
    return str[::-1]

input = "Python"
reversed_str = String_Rev(input)
print(reversed_str)


# 6 Count Vowels

def Count_Vowel(str):
    vowels = "aeiouAEIOU"
    count = 0
    for char in str:
        if char in vowels:
          count = count +1
    return count 

input1 = "Hello"
vowel_count = Count_Vowel(input1)  
print("Number of vowels:", vowel_count)


# 7 Prime Number 
def IsPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

num = 11  

if IsPrime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.") 



# 8 Factorial Calculation

def fact(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
n1 = 5
factorail_num = fact(n1)
if factorail_num is not None:
     print("Factorial of", num, "is", factorail_num)
else:
    print("Factorial is not defined for negative numbers.")
   
    
# 9: Fibonaci 
def fibonacci(n):
    seq = [0,1]
    if n<=2:
      return seq[:n]
    while len(seq)<n:
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)
    return seq  
num = 3
fibonacci_sequence = fibonacci(num)
print(fibonacci_sequence)


# 10:  List Comprehension
squared_numbers = [x**2 for x in range(1, 4)]
print(squared_numbers)
   



