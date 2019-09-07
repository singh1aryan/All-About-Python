# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:23:57 2019

@author: Aryan Singh
"""

'''

43. multiply strings
    num 1 and num2 given in strings, multiply them

    Example 1:
        Input: num1 = "2", num2 = "3"
        Output: "6"

    Approaches:
    1. string manipulation
'''

# convert to int and multiply - not allowed
# make a dp sort of array and then use that to fill it and then convert back to the string
# useful link - https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
def multiply(num1, num2):
    m=len(num1)
    n=len(num2)
    pos = [0 for i in range(m+n)]
    print(pos)
    for i in reversed(range(len(num1)-1)):
        for j in reversed(range(len(num2)-1)):
            print(i,j)
            p1 = i+j
            p2 = i+j+1
            mul = (num1[i]-'0')*(num2[j]-'0')
            sum = mul + pos[p2]
            pos[p1]+= sum/10
            pos[p2] = sum%10
    print(pos)

multiply("2","3")

