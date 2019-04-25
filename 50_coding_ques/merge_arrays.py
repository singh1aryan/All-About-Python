'''
8. Merge K Arrays

Question: 
    Given k sorted arrays, merge them into a single sorted array.

Eg:
    merge({{1, 4, 7},{2, 5, 8},{3, 6, 9}}) = {1, 2, 3, 4, 5, 6, 7, 8, 9}

Approach:
    merge 2 arrays
    repeat this for every pair till we have one
'''

def mergeArrays(arr):
    i=0
    j=len(arr)
    while i<j:
        ar = merge2Arrays(arr[i], arr[i+1])
        arr.append(ar)
        i+=2
    return arr[-1]
        
def merge2Arrays(a1, a2):
    i=0
    j=0
    newarray = []
    while i<len(a1) and j<len(a2):
        if a1[i] < a2[j]:
            newarray.append(a1[i])
            i+=1
        else:
            newarray.append(a2[j])
            j+=1
            
    for k in range(i, len(a1)):
        newarray.append(a1[k])
    
    for k in range(j, len(a2)):
        newarray.append(a2[k])
        
    return newarray

print(merge2Arrays([1,2,4],[3,6,9]))
print(mergeArrays([[1, 4, 7],[2, 5, 8],[3,6,9]]))

'''
Merge K lists - linked list:
    1. simple approach, O(N^2)
    2. min heap 
    3. divide and conquer
    
'''