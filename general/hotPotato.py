# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:27:03 2019

@author: Aryan Singh
"""

'''

 To begin, let’s consider the children’s game Hot Potato. 
 In this game (see Figure 2) children line up in a circle 
 and pass an item from neighbor to neighbor as fast as 
 they can. At a certain point in the game, the action 
 is stopped and the child who has the item (the potato) 
 is removed from the circle.  Play continues until only 
 one child is left.

'''

# importing the python queue
import queue

def hot_potato(nameList, num):
    
    q = queue.Queue(maxsize=20) 
    for name in nameList:
        q.put(name)
    
    while q.qsize()>1:
        for i in range(num):
            q.put(q.get())
            
        q.get()
    
    return q.get()

print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7)) 