'''
Q) Remove duplicates from a list

Approaches:
    python: - make it a set, and then convert back to list
    java: - 

'''

def remove_duplicates(arr):
    return list(set(arr))

print(remove_duplicates([1,2,3,4,5,2,3])) # 1,2,3,4,5

def remove_duplicates1(arr):
    newlist = []
    for i in arr:
        if i not in newlist:
            newlist.append(i)
            
    return newlist
            
print(remove_duplicates1([1,2,3,4,2,3,4])) # 1,2,3,4