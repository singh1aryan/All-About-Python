# Given an array nums of length n. All elements appear in pairs except one of them. Find this single element that appears alone.
# Pairs of the same element cannot be adjacent:

# [2, 2, 1, 2, 2] // ok
# [2, 2, 2, 2, 1] // not allowed

nums = [2,2,1,2,1,3]
# find the repeating element
def repeating(nums):
    a = {1}
    for i in nums:
        if i in a:
            return i
        else:
            a.add(i)
    print(a)

repeating(nums)