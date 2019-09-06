# common way to backtrack is this
# we have a for loop over the stuff we need
# we have the base case where the length is 0
# this is sort of more specific to python as we can easily do digits[1:] which is a subarray
# then the base case says that when the length is 0 - the condition where we add the fucking combination
# or whatever we have to add
phone = "abc"
output = []
def backtrack(combination, next_digits):
    # if there is no more digits to check
    if len(next_digits) == 0:
        output.append(combination)
        
    else:
        for letter in phone:
            backtrack(combination + letter, next_digits[1:])

backtrack("", "234")
# print(output)

# b = [1,2,3]
# print(b[:-1])


def sublist(nums):
    res = []
    dfs(nums, 0, [], res)
    return res

def dfs(nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        dfs(nums, i+1, path+[nums[i]], res)
    

print(sublist([1,2]))
