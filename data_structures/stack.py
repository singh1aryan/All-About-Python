# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:56:17 2019

@author: Aryan Singh
"""

# stacks, implementation and questions


import queue 
  
L = queue.LifoQueue(maxsize=6) 
  
# qsize() give the maxsize of 
# the Queue 
print(L.qsize()) 
  
# Data Inserted as 5->9->1->7,  
# same as Queue 
L.put(5) 
L.put(9) 
L.put(1) 
L.put(7) 
L.put(9) 
L.put(10) 
print("Full: ", L.full()) 
print("Size: ", L.qsize()) 
  
# Data will be accessed in the 
# reverse order Reverse of that 
# of Queue 
print(L.get()) 
print(L.get()) 
print(L.get()) 
print(L.get()) 
print(L.get()) 
print("Empty: ", L.empty()) 

q = queue.LifoQueue(maxsize=10)

