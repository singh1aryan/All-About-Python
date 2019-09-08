# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# "ababcbaca", "defegde", "hijhklij".
# partition in a way that letters are unique in each partition
# like a letter from 1st one isn't in the 2nd one and so on
# Approachhhh ---------------------------
# use a hashmap/dictionary maybe to keep the count, cause we don't want the stuff from back
# looks backtracking as might have to go back or forth
# or maybe not, can get it without, cause it's partitioning
# look for the last occurence of a, then b, 

def partition(str):
    b={}
    for i in range(0,len(str)):
        index=i
        for j in range(i+1, len(str)):
            if str[i]==str[j]:
                index = j
        if str[i] not in b:
            b[str[i]] = (i, index)

    m=[]
    for i in b:
        m.append(b[i])
    print(m)
    m.sort()
    i=0
    res = []
    while i<len(m):
        l = m[i][0]
        r = m[i][1]
        # if the upper bound is more, change it, simply
        j=i+1
        u=r
        while j<len(m) and m[j][0]<r:
            if m[j][1]>r:
                r = m[j][1]
                u=r
            j+=1
        i=j
        res.append(u-l+1)
    
    print(res)
        

S = "ababcbacadefegdehijhklij"
partition(S)