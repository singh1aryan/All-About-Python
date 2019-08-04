# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 10:44:00 2019

@author: Aryan Singh
"""

# return true if palindrome


def lower_casae(x):
    return x.lower()

def check_palindrome(s):
    l=0
    r=len(s)-1
    while l<r:
        if s[l]==s[r]:
            continue
        else:
            return False
        l+=1
        r-=1
    return True
    
def check_palindrome_recursive(s):
    if len(s)<2:
        return True
    
    if s[-1]==s[0]:
        return check_palindrome_recursive(s[1:-1])
    
    else:
        return False
    
if check_palindrome("abababa"):
    print("Plaindrome")
else:
    print("Not a palindrome")
        
if check_palindrome_recursive("abababba"):
    print("True")













