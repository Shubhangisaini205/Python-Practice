# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"


nums = [2, 7, 11, 15]
target = 9

def Targetsum(nums,target):
    for i in range(len(nums)):
       for j in range(i+1,len(nums)):
           if nums[i]+nums[j]==target:
               return [i,j]
            
    return -1 

print(Targetsum(nums,target))

