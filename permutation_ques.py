# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 01:30:58 2019

@author: Aryan Singh
"""

# p(x)=0.1, p(y)=0.4,p(z)=0.5
# 5 trials
# find the total outcomes for atleast one Y and one Z (out of 5 trials)

numbers = []
s = ""

x=""
y=""
z=""

def add(x):
    if len(x)==5: 
        numbers.append(x)
        print(x)
    else:
        add(x+"x")
        add(x+"y")
        add(x+"z")
        
add("")
print(len(numbers))

"""
print("object")
print(numbers[3])
print(len(numbers))
"""
a = len(numbers)
index = []

# add the index to a list which don't have atleast one 'y' and 'z'
def add_index(x):
    for i in range(0,a-1):
        if numbers[i].count("y")==0:
            index.append(i)
        elif numbers[i].count("z")==0:
            index.append(i)
    remove()

# remove the strings on those characters
def remove():
    for i in range(0,len(index)):
        numbers.pop(i)


add_index(numbers)
print(len(numbers))   

def find_prob(numbers,a):
    for i in range(0,len(numbers)):
        a += 0.1**numbers[i].count("x") + 0.4**numbers[i].count("y") + 0.5**numbers[i].count("z") 
        print(a)
    return a

print(find_prob(numbers,0))










