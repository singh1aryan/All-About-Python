# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:23:58 2019

@author: Aryan Singh
"""

# permutation lists / arrays

'''
[1,2,3]
we cannot separate this into [1], [2,3] like the strings
we should keep it in one array, and have a pointer going through it
we would swap the elements and call in recursively
we would have to swap back again to 'not chagnge' anything in the array

we would be swapping the index with itself, but that does not change anything
it is recursive and that's why we need the base case

Example: [1,2,3]
[1,2,3] - itself
[1,3,2] - swaps 2,3 because its a recursive call and goes deep
[2,1,3] - swaps 1,2 as the first deep recusive calls are finished now

follows similar pattern

'''

def permutation_array(array,results):
    permutation(array,0,results)
    return results
    
def permutation(a, start, results):
    if start>=len(a):
        results.append(a[:])
    else:
        for i in range(start,len(a)): # values would duplicate if we have '0' here
            swap(a,start,i)
            permutation(a,start+1,results)
            swap(a,start,i)
    
def swap(arr, i, j):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    
res = []
print(permutation_array([1,2,3], res))