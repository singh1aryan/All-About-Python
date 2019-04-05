'''
delete:
    with head pointer
    without the head pointer
Linked list 

node:
    node - next
    int - data
'''

def delete_with_head(head, target):
    while head.next.data is not target:
        head = head.next
    head = head.next.next

'''
# node is the reference of the node we want to delete
# We do not know the head

2 approaches:
    1. move the data to the left and then like the node to None
    2. Move the data and node once
'''
def delete_without_head(node):
    node.data = node.next.data
    ndoe.next = node.next.next