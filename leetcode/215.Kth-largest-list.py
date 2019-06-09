'''

215. Kth largest in a list

Solution:
    1. we will use a heapq - python

'''

import heapq # we don't have to import in leet code


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # min or max at any point
        # for smallest we can use min heap
        heap = []
        
        # heapq is the min heap
        
        for num in nums:
            heapq.heappush(heap, -num)
            
        for _ in range(k):
            res = heapq.heappop(heap)

        return res * -1
