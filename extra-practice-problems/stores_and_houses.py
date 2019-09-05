# returns the nearest house in the second array
# so if we have 5,10,17 - returns an array of numbers nearest to these numbers
def house(h, s):
    s=sorted(s)
    a=[]
    for i in h:
        b = binarysearch(s, i)
        a.append(b)
    return a

def binarysearch(arr, target):
    l=0 
    r=len(arr)-1
    while(l<r):
        mid = int((l+r)/2)
        if r-mid == 1:
            if abs(target-arr[mid])>abs(target-arr[r]):
                return arr[r]
            else:
                return arr[mid]
        if arr[mid]==target:
            return target
        if arr[mid]>target:
            r=mid
        else:
            l=mid


print(house([5,10,17], [1,5,20,11,16]))