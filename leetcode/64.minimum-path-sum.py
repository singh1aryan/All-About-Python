'''
find the minimum path 
from the top left to bottom right

medium level

Backtracking or I would say dynamic programming

visualize this as a new grid array:
    we change the values
    if it's a row or column, just add the previous value
    else add the minimum to it
    this way we would end with the minimum cost or sum at the end
    simply return that
    
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a = []
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i-1]
            
        for i in range(1, len(grid)):
            grid[i][0] += grid[i-1][0]
            
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
            
        
        
                    
        # grid[0][0]+=grid[0][1]
        print(grid)      
        return grid[-1][-1]