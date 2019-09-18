"""
 - pick an unvisited node
 - check children - if explored or not
 - add to visited if not explored
 - if children not explored - add to stack,temp and choose another one again - recursive
"""
def buildOrder(nums):
    temp = set()
    visited = set()
    stack = [] # the final output we need
    for i in range(len(nums)):
        if i not in visited:
            visit(i,nums,visited,temp,stack)

    # temp will be empty here, perm will have all the nodes
    return stack

def visit(i,nums,visited,temp,result):
    if i in temp:
        return None # this means there is a cycle

    # if not in visited
    if i not in visited:
        temp.add(i)

        # exploring neighbors
        for index in nums[i]:
            visit(index,nums,visited,temp,result)
        
        # add to visited
        visited.add(i)
        temp.remove(i)
        result.append(i)

print(buildOrder([[0],[1,0],[2,0],[3,1,2],[4,3]]))# prints 0,1,2,3,4