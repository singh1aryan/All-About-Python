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

# def value(root):
#     if not root.left and not root.right:
#         return  root.left + root.right
    
#     return value(root.left)+value(root.right)+helper(root)

# def helper():
#     # find the product of leftmost and rightmost node of the right and left node

# for e = 1 to m do
#     Let u and v be endpoints of e
#     if find(u) != find(v): # Not in same component
#         T = T ∪ {e}
#         Union(find(u), find(v)) # Merge components
#     end if
# end for

def value(array):
    s = array[0]
    for i in range(1,len(array)):
        s += array[i]
        s += array[i-1]*array[i]
    return s

def height(node): 
    if node is None: 
        return 0 ; 
    return 1 + max(height(node.left) ,height(node.right)) 
  
# Function to get the diamtere of a binary tree 
left_height=0
right_height=0
def diameter(root):  
    # Base Case when root is None or after leaf node 
    if root is None: 
        return 0; 
  
    left = diameter(root.left) 
    right = diameter(root.right) 
   
    a = max(left, right)
    return max(left_height + right_height + 1, a)