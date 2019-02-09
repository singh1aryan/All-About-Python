# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 00:03:33 2019

@author: Aryan Singh
"""

#lists in python
# structure to store data in python

f = ["aryan","para2","diwank","kkft9"] #just like an array
multi = ["A", 9, "aryan"] #lists dont have a type in python

print(f)
print(f[-2]) # negative goes from the back
print(f[1:]) # prints all elements from 1
print(f[1:3]) # from 1 to 3, 3 excluded

# this is basically easier and shorter 'for' loop

# modify the value

f[1] = "Mike" # changes the value at index 1
print(f[1])

# LIST FUNCTIONS

lucky_nums = [1,2,3,4]
friends = ["a","b","c","d"]

# functions to modify and get info about list

friends.extend(lucky_nums) # adds another list
print(friends)
friends.append("Arnold")
print(friends)

friends.insert(1,"Clark")
print(friends)
friends.remove("Arnold")
print(friends)

friends.pop() # removes the last element in the list

print(friends.index("b"))# check to see if some element is there

print(friends.count("a"))# counts the instances

friends.sort()# sorts the list
friends.reverse()

friends2 = friends.copy()# copying the list to friends2














