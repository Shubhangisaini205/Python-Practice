# 1. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]

input = [64, 25, 12, 22, 11]

for i in range(len(input)):
    minIndex=i
    for j in range(i+1,len(input)):
        if input[j]< input[minIndex]:
            minIndex = j

    # // swap the elements   
    temp = input[i]
    input[i] = input[minIndex] 
    input[minIndex]= temp
    
print(input)      