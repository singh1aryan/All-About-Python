import collections
import heapq
# minimum substring window with another string
def minimum_window(s, t):
	need = collections.Counter(t)
	l,r,i,j, missing = 0,0,0,0,len(t)

	while r<len(s):
		# print(need)
		if need[s[r]]>0: 
			missing -=1
		need[s[r]] -=1
		r+=1

		while missing == 0:
			if j==0 or r-l < j-i:
				print(s[i:j])
				i,j = l,r
			need[s[l]] += 1
			if need[s[l]]>0: 
				missing+=1
			l+=1
	return s[i:j]

# a = minimum_window("acbdnssaracbn", "abn")
# print(a)

import collections
# group the people according to their id's and their group size
def groupThePeople(groupSizes):
        count = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)

       	# print(count)
        # return [l[i:i + s]for s, l in count.items() for i in range(0, len(l), s)]
        b = []
        for s, l in count.items():
        	# print(s, l)
        	for i in range(0, len(l), s):
        		b.append(l[i:i+s])
        # print(b)
        return b

# a = groupThePeople([3,3,3,3,3,1,3])
# print(a)

# count the sqaures in a 2d matrix - all 1's that make a square
def countSquares(matrix):
    c=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i>0 and j>0 and matrix[i][j]==1:
                matrix[i][j] = min(matrix[i-1][j-1], min(matrix[i-1][j], matrix[i][j-1])) + 1
                
            c += matrix[i][j]
    # print(matrix)
    return c

# smallest divisor such that all divisions sum upto threshold
def smallestDivisor(A, threshold):
    l,r = 1, 10**6
    while l < r:
        m = (l + r) / 2
        if sum((i + m - 1) / m for i in A) > threshold:
            l = m + 1
        else:
            r = m
    return l

# a = smallestDivisor([1,2,5,9],6)
# print(a)

# delete nodes where the sum = 0
def deleteTreeNodes(nodes, parent, value):
    void = set()

    for i in range(nodes - 1, 0, -1):
        value[parent[i]] += value[i]
    
    print(value)
    res = 0
    for i,v in enumerate(value):
        if v != 0:
            if parent[i] not in void:
                res += 1
            else:
                void.add(i)
        else:
            void.add(i)
    return res

nodes = 7
parent = [-1,0,0,1,2,2,2]
value = [1,-2,4,0,-2,-1,-1]
# parent index is smaller, start from the right
# check if already seen the parent or not
# increase whenever you see the parent - have to check in values ==0 and non-repeated parents
# a = deleteTreeNodes(nodes, parent, value)
# print(a)

# trapping rain water
def trap(height):
    a = 0
    for i in range(0, len(height)):
        l_max = max(height[0:i+1])
        r_max = max(height[i:])
        a += min(l_max, r_max)-height[i]
        print(a, i)
        
    return a

# largest rectangle area - array of numbers given
def largestRectangleArea(heights):
    s = []
    s.append(-1)
    m = 0
    for i in range(0,len(heights)):
        while s[-1]!=-1 and heights[s[-1]]>=heights[i]:
            m = max(m, heights[s.pop()]*(i-s[-1]-1))
        s.append(i)
    while s[-1]!=-1:
        m = max(m, heights[s.pop()]*(len(heights)-s[-1]-1))
    return m
        

# maximum rectangle


# perfect squares
# find the minimum number of perfect squares which add up to num
def squares(num):
	if num <= 3:
		return num

	res = num
	for x in range(1, num+1):
		temp = x*x
		if temp > num:
			break
		else:
			res = min(res, 1 + squares(num - temp))
	return res

def squares_dynamic(n):
	dp = [float('inf')]*(n+1)
	dp[0]=0
	for i in range(1, n+1):
		for j in range(1, n+1):
			if j*j<=i:
				dp[i] = min(dp[i], dp[i-j*j] +1)
	return dp[n]


# buildings with obstacles given
def shortest_distance_from_buildings(matrix):
	def bfs():
		while s:
			a = s.pop(0)
	
	s = []
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			bfs()
	

def top_k_frequent_elements(nums, k):
	# nums = [1,1,1,2,2,3], k = 2
	count = collections.Counter(nums)
	heap = []
	for num in count:
	    if len(heap) < k:
	        heapq.heappush(heap,(count[num],num))
	    elif count[num] > heap[0][0]:
	        heapq.heapreplace(heap,(count[num],num))

	result = []
	heap.sort()
	heap.reverse()
	for item in heap:
		result.append(item[1])
	return result


# lfu cache
# linked list questions
# double linked list
# recursion
# trees - bst, binary
# tries

# Given a non-negative integer num represented as a string, 
# remove k digits from the number so that the new number is the smallest possible.
def removeKDigits(num, k):
	numStack = []
	for digit in num:
		while k and numStack and numStack[-1]>digit:
			numStack.pop()
			k-=1
		numStack.append(digit)

	finalStack = numStack[:-k] if k else numStack

	print(finalStack)
	return ''.join(finalStack).lstrip('0') or '0'


# you are given k transactions and you have to return max sell-buy
# dp question with some sort of matrix thing
def maxProfitWithKTransactions(prices, k):
	pass


def main():
	# a,b,c,d = squares_dynamic(1) ,squares_dynamic(20), squares_dynamic(45), squares_dynamic(13)
	# nums = [1,1,1,2,2,3]
	# k = 2
	# print(top_k_frequent_elements(nums, k))
	num = "1432219"
	k = 3
	print(removeKDigits(num, k))

if __name__ == '__main__':
	main()