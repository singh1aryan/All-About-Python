
# linked lists in python

class Node():
    
    def __init__(self, val):
        self.val = val;
        self.next = None
        
class LinkedList():
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size=0
        self.head = None
    
    # value at index in linked list
    def get(self, index):
        
        if self.head is None:
            return -1
        
        curr = self.head
        for i in range(0,index):
            curr = curr.next
        return curr.val            
    
    # add val node to head
    def add_to_head(self, val):
         #curr = self.head
        
        #creating a new node
        node = Node(val)
        
        node.next = self.head
        self.head = node
        
        self.size+=1
    
    def add_to_tail(self, val):
        node = Node(val)
        curr = self.head
        for i in range(0,self.size):
            curr=curr.next
        curr.next=node
        
    
    def size(self):
        return self.size
    
    
    def delete_head(self):
        self.head = self.head.next
        
        
    def delete_tail(self):
        curr = self.head
        for i in range(0,self.size):
            curr=curr.next
        curr.next  = None
        
        
    def delete_at_index(self,index):
        curr = self.head
        if index is 0:
            self.delete_head(self)
        else:
            for i in range(0,index-1):
                curr=curr.next
            curr.next=curr.next.next
        
        self.size-=1

def sortedSearch(head, target):
    currNode = head
    while currNode is not None and currNode.data<target:
        if currNode.data == target:
            return True
        else:
            currNode = currNode.next
        return False

        
# self is only for reference, we don't care about it when initializing
list_one = LinkedList()
list_one.add_to_head(3)
list_one.add_to_head(4)
print(list_one.size)
        
        
        
        
        
        
        
        
        
        