# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:50:49 2019

@author: Aryan Singh
"""

# big o with loops and programs

def ex2( n ):
    count = 0
    for i in range( n ) :
        count += 1 # we have count here
        for j in range( n ) :
            count += 1
    return count

# O(n^2)
def ex3( n ):
    count = 0
    for i in range( n ) :
        for j in range( n ) :
            count += 1
    return count


