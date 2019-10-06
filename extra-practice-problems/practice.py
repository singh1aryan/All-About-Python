def quicksort(nums):
    if len(nums)<=1:
        return nums
    pivot = nums[len(nums)//2]
    left = [x for x in nums if x<pivot]
    middle = [x for x in nums if x==pivot]
    right = [x for x in nums if x>pivot]
    return quicksort(left)+middle+quicksort(right)


# print(quicksort([1,3,4,2,6,5]))

"""
understand the base case, don't just write anything
we divide the array into left,right and middle
then we combine back to form the array again

quicksort - we make left,right and middle arrays and then combine them
we do this recursively but in a sense that we return an array at the end
"""

# b = {0:1,1:3}
# print(b[::-1])
# a= []
# for i in range(1000000):
#     # for j in range(1000000):
#     a.append([i])
# print(a[0])

# subsets with this, woah
a=[]
def rec(soFar, rest):
    if len(rest)==0:
        a.append(soFar)
    else:
        rec(soFar + [rest[0]], rest[1:])#inclusion
        rec(soFar, rest[1:])#exclusion
# rec([],[1,2,3])
# print(a)
import sys
sys.setrecursionlimit(50)
per = []
def permute(a,b):
    if len(a)==3:
        print(a)
        per.append(a)
    else:
        for i in range(len(b)):
            r = b[0:i]+b[i+1:]#exclusion
            print(r)
            permute(a+[b[i]], r)#inclusion

# permute([],[1,2,3])
print(per)


# stack = []
# stack.append(root)
# while len(stack)>0:
#     a = stack.pop()
#     visited_set.add(a)
#     if a is leaf_node:# a does not have neighbors
#         break
#     if a has neighbors:
#         stack.append(neighbors)

# if length of visited_set == number of nodes:
#     return True
# else:
#     return False
dp = [[1,2,3,4],[4,3,2,4],[2,20,100,30]]
n=3
m=4
for i in range(n):
    for j in range(m):
        if i==0:
            continue
        else:
            print(i,j)
            dp[i][j] += min(dp[i-1][0:j] + dp[i-1][j:])#min of exluding that color
            
print(dp)