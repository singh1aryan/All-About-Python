# Insertion sort
# Wiki page - 
# Insert element at the right place - sort every element as you go

# def pseduo_insertion(nums):
#     for i in range(0, len(nums)):
#         # find the place for the i'th element in the subarray from 0,i
#         # take a for loop from 0,i and find the correct place for ith element 
#         # insert it there
#         break

def insertion_sort(nums):
    for i in range(1,len(nums)):
        j=i
        while j>0 and nums[j-1]>nums[j]:
            nums[j],nums[j-1] = nums[j-1], nums[j]
            j=j-1        

    return nums

# Time Complexity - O(N), O(N^2), O(N^2) - Best, Average, Worst
# Space Complexity -  O(1) 
print(insertion_sort([1,3,4,2,6,5]))
print(insertion_sort([1,3,24,2,6,5]))
print(insertion_sort([1,13,4,2,6,5]))
print(insertion_sort([11,3,4,2,6,5]))