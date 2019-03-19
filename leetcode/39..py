# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 00:31:56 2019

@author: Aryan Singh
"""

'''
leet code problem
    39. Combination Sum

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Strategies:
    1. Recusrive + Path finding
    2. This is advanced version of 2 sum
'''

l = []
def sumTarget(array, target):
    l=[]
    array.sort()
    dfs(array, target, 0, [], l)   
    return l
    
def dfs(nums, target, index, path, res):
    if target < 0:
        return
    if target == 0:
        res.append(path)
        return
    for i in range(index, len(nums)):
        dfs(nums, target-nums[i], i, path+[nums[i]], res)
        
print(sumTarget([2,3,4],7))
print(sumTarget([2,3,7],7))

'''
2nd approach
Common approach for dfs, backtracking - for search and path


def solve(array, target):
    l=[]
    array.sort()
    dfs1(array, target, 0, [], l)   
    return l

def dfs1(nums, remain, start, path, res):
    if remain < 0:
        return
    elif remain == 0:
        res.append(path)
    for i in range(start, len(nums)):
        path.append(nums[i])
        dfs(nums, remain - nums[i], i, path, res)
        path.remove(nums[len(nums)-1])
        
print(solve([2,3,4],7))
'''