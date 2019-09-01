list = []

def binarysearch(alist, target):
    if len(alist)==0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == target:
            return True
        elif alist[midpoint]>target:
            return binarysearch(alist[:midpoint], target)
        else:
            return binarysearch(alist[midpoint+1:], target)    


print(binarysearch([1,2,3,4,5,6,7], 5))