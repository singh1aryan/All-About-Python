# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 05:21:58 2019

@author: Aryan Singh
"""



# using the python list 
class Stack_Python_List:
    def __init__(self):
        self._theItems = list()
        
    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self._theItems)
    
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at empty stack"
        return self._theItems[-1]
    
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self._theItems.pop()
    
    def push(self, item):
        self._theItems.append(item)
        
        
# using the linked list - not the python list
        
class Stack_Linked_list:
    def __init__(self):
        self._top = None
        self._size = 0
        
    def isEmpty(self):
        return self._top is None
    
    def __len__(self):
        return self._size
    
    def peek(self):
        assert not self.isEmpty(), "Cannot peek from the empty stack"
        return self._top.item
    
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from the empty stack"
        node = self._top
        self._top = self._top.next
        self._size-=1
        return node.item
    
    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size+=1

class _StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link
        
stack_one = Stack_Python_List()
stack_one.push(2)
stack_one.push(3)
stack_one.push(4)
stack_one.push(5)
print(stack_one.pop()) #prints 5, the top element

stack_two = Stack_Linked_list()
stack_two.push(2)
stack_two.push(3)
stack_two.push(4)
stack_two.push(6)
print(stack_two.pop()) #prints 6, the top element

