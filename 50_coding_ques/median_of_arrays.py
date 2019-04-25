'''
Question : Find the median of two sorted arrays.
    1. Array length is the same
    2. Arrays are sorted
Eg:
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
median(arr1, arr2) = 3.5
'''

import numpy as np
import statistics

a1 = [1,2,3,4]
a2 = [3,4,5,6]

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

def median_array(arr1, arr2):
    ''' find the median of 2 arrays'''
    a = []
    a.append(statistics.median(a1))
    a.append(statistics.median(a2))
    print(statistics.median(a))

median_array(a1,a2)
median_array(arr1,arr2)

'''
approach 2:
    - we merge the arrays and then take the median according to the length
    - median can be taken by the statistics.median method
'''

def merge_array(a1, a2):
    i=0
    j=0
    new_array = []
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            new_array.append(a1[i])
            i+=1
        else:
            new_array.append(a2[j])
            j+=1

    for k in range(i,len(a1)):
        new_array.append(a1[k])
        
    for k in range(j,len(a2)):
        new_array.append(a2[k])

    return new_array
    
arr = merge_array(arr1, arr2)
print(statistics.median(arr))