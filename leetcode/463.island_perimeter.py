# You have one big island of connected 1's in a 2d array
# return the perimeter of the island
# Trick here is to count the neighbors -> if you got 4 neighbors, add 0, if 3, add 1 and so on
def islandPerimeter(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    count=0
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            s=0
            if grid[i][j]==1:
                if i>0 and grid[i-1][j]==1:
                    s+=1
                if j>0 and grid[i][j-1]==1:
                    s+=1
                if i<len(grid)-1 and grid[i+1][j]==1:
                    s+=1
                if j<len(grid[0])-1 and grid[i][j+1]==1:
                    s+=1
                if s==0:
                    return 4
            if s==0:
                continue
            count += (4-s)
    return count