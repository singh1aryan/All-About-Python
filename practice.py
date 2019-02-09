# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 22:37:45 2019

@author: Aryan Singh
"""

def fn(x):
    return x

phrase = "giraffe"
print("Good one\nOne")
print("Good one\"nOne")# \" prints it literally
print(phrase)
print(2+3)
print(fn(6))
print("Cool") # functions dont have a return type

word = "WRRE"
print(word.lower());# changes to lower case, but only reference
print(word.islower())# this returns false

print(len("abcd"))
print(word[3])
a = int(word.index("R"))
print(a)

word = word.replace("W","D")# if we just do word.replace, then we wont get the D
print(word)

print(10%3)# gives us the remainder 

number = 5;
print(str(number) + "number")

print("name")