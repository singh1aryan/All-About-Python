# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 00:08:53 2019

@author: Aryan Singh

some points on binary trees - http://cslibrary.stanford.edu/110/BinaryTrees.pdf
"""

def lookup(node, target):
    if node == None:
        return False
    else:
        if target < node.data:
            return lookup(node.left, target)
        else:
            return lookup(node.right, target)

