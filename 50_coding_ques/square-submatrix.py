# Question: Given a 2D array of 1s and 0s, find the largest square subarray of all
# 1s.
# Eg. Given a 2D array of 1s and 0s, find the largest square subarray of all 1s.
# Answer: https://www.byte-by-byte.com/squaresubmatrix/

"""
First impression - dfs maybe, something like number of islands
Way - 
Brute force - 
optimization - 
"""

def square(grid):
    m=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                m=max(m,square_helper(grid,i,j))#check for every square
    return m

def square_helper(grid,i,j):
    if i==len(grid) or j==len(grid[0]):
        return 0
    if not grid[i][j]:
        return 0
    return 1+min(min(square_helper(grid,i+1,j),square_helper(grid,i,j+1)),square_helper(grid,i+1,j))

# print(square([[1, 1, 1, 0],[1, 1, 1, 1],[1, 1, 0, 0]]))


"""
dynamic programming answer
"""
def dynamic(grid):
    
    dp = [i for i in grid]
    a=[0]*(len(grid[0])+1)
    dp.insert(0,a)
    ans = 0
    for i in range(1,len(dp)):
        dp[i].insert(0,0)
    for i in range(1,len(dp)):
        for j in range(1,len(dp)):
            if dp[i][j]==0: continue
            else:
                m = 1+min(min(dp[i-1][j],dp[i][j-1]),dp[i-1][j-1])
                dp[i][j] = m
                ans = max(m,ans)
    return ans

grid = [[1, 1, 1, 0],[1, 1, 1, 1],[1, 1, 0, 0]]
print(dynamic(grid))


    