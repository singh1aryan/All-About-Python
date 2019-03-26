# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:36:00 2019

@author: Aryan Singh
"""

'''
Your code should output a single line of text, starting with “true” (the theorem was proved) or
“false”, followed by a space and a integer indicating the number of times the your code applied
the resolution rule while attempting to prove the theorem.
For example:
false 42

A V -B
'''
import itertools

symbols = {'^', 'V', '→', '↔'} # Symbols for easy copying into logical statement

statement = '~(A V B) ↔ (~A V ~B)'

#args are number of variables
def generate_table(a,l,r):
    if l==r:
        print(a)
    else:
        for i in range(l,r+1):
            swap(a,i,l)
            generate_table(a,l+1,r)
            swap(a,i,l) # backtrack
            
def swap(arr, i, j):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j]=temp
        
string = "TFT"
n = len(string) 
a = list(string) 
#generate_table(a,0,n-1)

l2=[]
def generate(n,l1,l3):
    if n==0:
        if l1 not in l2:
            print(l1)
            l2.append(l1)
    if n>0 :
        for i in (0,2):
            generate(n-1,l1+'T',l3)
            generate(n-1,l1+'F',l3)
    
generate(3,'',[])
#print(l3)

def generate_loops(n,l=[]):
    if not n:
        print(l)
    for i in [True, False]:
        generate_loops(n-1,l+[i])
        
#generate_loops(3,[])
#table = list(itertools.product([False, True], repeat=3))
#print(table)