# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:44:54 2019

@author: Aryan Singh
"""

'''

The count-and-say sequence is the sequence of integers 
with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

'''
class Solution(object):
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                for digit, group in itertools.groupby(s))
        return s