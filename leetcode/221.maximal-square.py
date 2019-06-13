'''

221. maximum square

given a 2D matrix, return the square with only 1
    Example:
    
    Input: 
    
    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0
    
    Output: 4

we go for dynamic programming, break the problem
into smaller problems and then solve it

Easy java code

public class Solution {
    public int maximalSquare(char[][] matrix) {
        int rows = matrix.length, cols = rows > 0 ? matrix[0].length : 0;
        int[][] dp = new int[rows + 1][cols + 1];
        int maxsqlen = 0;
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                if (matrix[i-1][j-1] == '1'){
                    dp[i][j] = Math.min(Math.min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1;
                    maxsqlen = Math.max(maxsqlen, dp[i][j]);
                }
            }
        }
        return maxsqlen * maxsqlen;
    }
'''

# edge cases missing here
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        grid = []
        f=1
        for i in matrix:
            a=[0]
            if f == 1:
                for k in i:
                    a.append(0)
                grid.append(a)
                f=0
                continue
            for j in i:
                a.append(int(j))
            grid.append(a)
            
        print(grid)
        ma = 0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix)):
                if matrix[i][j]=='1':
                    grid[i][j] = min(grid[i-1][j-1], min(grid[i-1][j], grid[i][j-1]))+1
                    ma = max(grid[i][j], ma)
                    
        print(grid)
        return ma*ma
    
'''
some changes needed here

'''