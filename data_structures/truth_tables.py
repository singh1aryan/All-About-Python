# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:26:12 2019

@author: Aryan Singh
"""

'''
generate truth tables
'''
import itertools
def solver1(num):
    table = list(itertools.product([False, True], repeat=num))
    print(table)

solver1(2)
solver1(3)

# using loop and recursion, for loop of 2 for true and false
l2=[]
def solver2(n,l1,l3):
    if n==0:
        if l1 not in l2:
            print(l1)
            l2.append(l1)
    if n>0 :
        for i in (0,2):
            solver2(n-1,l1+'T',l3)
            solver2(n-1,l1+'F',l3)
    
solver2(3,'',[])