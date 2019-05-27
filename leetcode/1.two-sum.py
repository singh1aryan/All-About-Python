# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:27:04 2019

@author: Aryan Singh

Leet code problem
    1. Two Sum

Java - effecient way
    1. Use a hash map
    2. Find the complement of the number at index 'i'
    3. complement is target - array[i]
    
"""

# 2 loops, O(N^2)
def two_sum_loop(array, target):
    for i in range(0,len(array)):
        for j in range(i,len(array)):
            if array[i]+array[j]==target:
                return i,j # prints the i,j together




print(two_sum_loop([1,2,3,4],7))
