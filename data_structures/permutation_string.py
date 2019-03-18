# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:09:40 2019

@author: Aryan Singh
"""

# permutations of a string

# recursive implementation


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