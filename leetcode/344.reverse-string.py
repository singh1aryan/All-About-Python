def reverseString0(str):
    s=""
    for i in reversed(str):
        s+=i
    return s

print(reverseString0("abcd"))

def reverseString(s):
        # recursive function - base case, back to base case
    l=0
    r=len(s)-1
    while l<r:
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1
    return s
            

print(reverseString(['a','b','c','d','e','f','g']))