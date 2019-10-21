# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 22:37:45 2019

@author: Aryan Singh
"""

# def fn(x):
#     return x

# phrase = "giraffe"
# print("Good one\nOne")
# print("Good one\"nOne")# \" prints it literally
# print(phrase)
# print(2+3)
# print(fn(6))
# print("Cool") # functions dont have a return type

# word = "WRRE"
# print(word.lower());# changes to lower case, but only reference
# print(word.islower())# this returns false

# print(len("abcd"))
# print(word[3])
# a = int(word.index("R"))
# print(a)

# word = word.replace("W","D")# if we just do word.replace, then we wont get the D
# print(word)

# print(10%3)# gives us the remainder 

# number = 5;
# print(str(number) + "number")

# print("name")

def threewaysort (l,i,j):
    if l[i]>l[j]:
        l[i],l[j]=l[j],l[i]
        print(i,j)
    if (j - i + 1) > 2:
        t = ( j - i + 1)/3
        # print(l, 1)
        threewaysort (l, i+t, j)
        # print(l, 2)
        threewaysort (l, i, j-t)
        # print(l, 3)
        threewaysort (l, i+t, j)

a = [3,5,1,4,8,3,9]
b = [2,1]
threewaysort(a,0,len(a)-1)
print(a)

def value(root):
    if not root.left and not root.right:
        return  root.left + root.right
    
    return value(root.left)+value(root.right)+helper(root)

def helper():
    # find the product of leftmost and rightmost node of the right and left node