'''
4. Find Duplicates
Question : 
    Given an array of integers where each value 1 <= x <= len(array), write
    a function that finds all the duplicates in the array.
Eg.
    dups([1, 2, 3])    = []
    dups([1, 2, 2])    = [2]
    dups([3, 3, 3])    = [3]
    dups([2, 1, 2, 1]) = [1, 2]

we can use HashMap in Java -- easier and more effecient
'''

def duplicates(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

print(duplicates([1, 2, 3]))
print(duplicates([1, 2, 2]))
print(duplicates([3, 3, 3]))
print(duplicates([2, 1, 2, 1]))

'''
Notes: 
    O(N) approach, using maps maybe
    single loop to check duplicates
    
'''

