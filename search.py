# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:54:20 2019

@author: Aryan Singh
"""

# searching in python


# linear search

def linear_search(arr,target):
    for i in arr:
        if i==target:
            return True
    return False

# linear search in sorted list

def linear_sorted_search(arr, target):
    for i in len(arr):
        if arr[i]==target:
            return True
        if arr[i]>target:
            return False
    return False

# find the smallest in the list

def smallest_in_list(arr):
    smallest = arr[0]
    for i in range(1,len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
    return smallest        
    
def larget_in_list(arr):
    largest = arr[0]
    for i in range len(arr):
        if largest<arr[i]:
            largest=arr[i]
    return largest








