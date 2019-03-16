# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 05:21:23 2019

@author: Aryan Singh
"""

# queues in python


# importing the python queue

# queue -- put() , get() , qsize() , full(), empty(), 

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