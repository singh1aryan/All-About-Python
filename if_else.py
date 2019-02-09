# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 10:21:44 2019

@author: Aryan Singh
"""

# # if else statements

is_male = True
is_female = False

if is_male:
    print("Male")
elif is_male or not(is_female):
    print("Both")
else:
    print("Female")
    
    # && is and
    # || is or
    # Don't have to use parenthesis
    
# replace elif with if, to print male and 'both'

# comparisons    


def max_num(list):
    return max(list)
    
print(max_num([2,3,4,5,6]))