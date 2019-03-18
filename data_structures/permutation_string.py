# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:09:40 2019

@author: Aryan Singh
"""

'''
recursive implementation of the string permutations
First method:
    1. uses the substring property of strings (not valid for arrays)
    2. 

'''


def permutationString(s, results):
    permutation("", s, results)
    return results
    
def permutation(prefix, suffix, results):
    if len(suffix)==0:
        results.append(prefix)
    else:
        for i in range(0,len(suffix)):
            permutation(prefix+suffix[i], suffix[0:i]+suffix[i+1:], results)
            
l = ['']
print(permutationString("abc", l))

'''
2nd implementation, using the swap method - smaller/easier in Python
    1. string
    2. starting index of string
    3. ending index of string
'''


def permutationString2(a,l,r):
    if l==r:
        print(a)
    else:
        for i in range(l,r+1):
            swap(a,i,l)
            permutationString2(a,l+1,r)
            swap(a,i,l) # backtrack
            
def swap(arr, i, j):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    
string = "ABC"
n = len(string) 
a = list(string) 
permutationString2(a,0,n-1)