# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 01:49:15 2019

@author: Aryan Singh
"""

'''
Introduction to Blockchain
    1. Try new things
    2. Explore exciting stuff

Source
https://medium.com/coinmonks/building-a-simple-blockchain-data-structure-with-python-e7ebd448647a

Here, I am going to build a simple blockchain data structure 
which is the foundation of Bitcoin. This data structure only 
is not enough to build even a simple cryptocurrency. 
But we have to start somewhere.


'''

import hashlib
print(hashlib.sha256(b"thello world").hexdigest())

'''
Hashing is a process which you turn anything 
(as long as you can represent it as a string) 
into a fixed 256 bit string

'''
print(hashlib.sha256(b"I am the best president. Ever.").hexdigest())
