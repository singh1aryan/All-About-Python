# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 18:49:08 2019

@author: Aryan Singh
"""

# for loops

for letter in "Aryan singh":
    print(letter) #prints one at a time
    print(len(letter)) #prints 1

arr = ["a","b","c","d","e"]
for l in arr:
    print(l)
    
for number in range(1, 1001):
    print(number)


ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
youngest = min(ages)
oldest = max(ages)
total_years = sum(ages)

squares = []
for x in range(1, 11):
    square = x**2
    squares.append(square)
    
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = []
for name in names:
    upper_names.append(name.upper())
    

