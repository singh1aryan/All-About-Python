'''
3. Matrix product
    Question : Given a matrix, find the path from top left to bottom right with the
    greatest product by moving only down and right.
Eg.
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    1 ‑> 4 ‑> 7 ‑> 8 ‑> 9
    
    2016
    [1, -2, 3]
    [-4, -5, ‑6]
    [7, 8, 9]
    1 ‑> -2 ‑> 3 ‑> ‑6 ‑> 9
    324

Approach:
    recursive:
        base case ?, we need the max again
        what is the subproblem here ? what are the edge cases?
'''

path = []
neg = 0
def product(arr, down, right, neg):
        
    if down >= len(arr):
        return 1
    if right >= len(arr[0]):
        return 1
    
    p = arr[down][right]
    
    return max(p*product(arr, down+1, right, neg), p*product(arr,down, right+1, neg))

arr = [[1,2,3],[4,5,6],[7,8,9]]
arr1 = [[1,-2,3],[-4,-5,-6],[7,8,9]]

print(product(arr, 0, 0, 0))
print(product(arr1, 0, 0, 0))

'''
Notes: 
we have to go down and right only, so those are the only 2 cases for recursion
we also have to handle negative values -- edge case
negative values would act differently for 0,0 and 3,3 and other indices

one way would be to check number of negative values
and then choosing min and max according to that

we also have a target thing here, we have to reach the bottom right
how do we check that ?
'''