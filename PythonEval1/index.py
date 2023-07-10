# 1=># a. Write a Python program that takes a string input from the user and prints out the reversed string.  
# For instance, if a user inputs: "Python is fun"

# Expected output:

# nuf si nohtyP


def Reverse(str):
    return str[::-1]

str = "Python is fun"

print(Reverse(str))


# 2.

employees = [
    {"name":"John","salary":3000,"designation":"developer"},
    {"name":"Emma","salary":4000,"designation":"manager"},
    {"name":"Kelly","salary":3500,"designation":"tester"}
]
max = -1
ans = {}
for item in employees:
    if max < item["salary"]:
        max = item["salary"]
        ans = item

print(ans)



