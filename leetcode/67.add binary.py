# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
def binary(num1, num2):
    a=[]
    i=len(num1)-1
    j=len(num2)-1
    carry=0
    while i>=0 or j>=0:
        sum=carry
        if i>=0:
            sum += int(num1[i])
            i-=1
        if j>=0:
            sum += int(num2[j])
            j-=1
        a.insert(0,sum%2)
        carry = sum//2

    if carry>0:
        a.insert(0,carry)
    print(a)

a = "1010"
b = "1011"
binary(a, b)

