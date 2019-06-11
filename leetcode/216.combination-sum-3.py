'''
216. COMBINATION SUM III

find the total combinations where 
k numbers sum upto n

Approach:
    1. recursive
    2. make a helper function
    3. recursion in for loop, adding and deleting items

'''

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        self.dfs(results, [], k, n, 1)
        return results
    
    def dfs(self, results, path, k, n, start):
        if len(path)>k:
            return
        if len(path) == k and sum(path) == n:
            if len(set(path)) == len(path):
                results.append(path)
                print(results)
            
        for i in range(start, 9):
            path.append(i)
            self.dfs(results, path, k, n, i+1)
            del path[-1]