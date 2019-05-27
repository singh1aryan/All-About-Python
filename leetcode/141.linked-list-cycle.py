# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:23:57 2019

@author: Aryan Singh
"""

'''

Linked list cycle
return true if there is a cycle in the linked list
general approach:
    1. slow and fast pointer
    2. if the slow pointer reaches the fast, then true


'''

class Solution(object):
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast=fast.next.next
            return False
        except:
            return False
        