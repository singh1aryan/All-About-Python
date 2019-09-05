# Example:
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

# Looks recursive on the first go, loops would take it too far
# Tracking the visiting might help, but a basic strategy of choose explore unchoose looks the case
# def letterCombination(str):
#     # we can avoid a dictionary by making something like this
#     a = ["0", "1", "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
#     num = []
#     # one way of doing is to separate out everything and then just use combination
#     # str - "23"
#     for i in str:
#         print(i)
#         for j in a[int(i)]:
#             num.append(j)

#     # num has abcdef now, we need all combinations of len(num) - which is 2
#     print(num)
#     n=[]
#     dfs(num, 2, "", 0, n)
#     print(n)


# def dfs(nums, k, str, curr, num):
#     if(len(str) == k):
#         num.append(str)
#     i=curr
#     while i< len(nums):
#         str += nums[i]
#         # we can continue if the first and last letter of str are in the same group
#         if ord(str[len(str)-1]) - ord(str[0]) < 3:
#             break 
#         dfs(nums, k, str, i+1, num)
#         str  = str[0:-1]
#         i+=1

# letterCombination("23")


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
            
    def backtrack(combination, next_digits):
        # if there is no more digits to check
        if len(next_digits) == 0:
            # the combination is done
            output.append(combination)
        # if there are still digits to check
        else:
            # iterate over all letters which map 
            # the next available digit
            for letter in phone[next_digits[0]]:
                # append the current letter to the combination
                # and proceed to the next digits
                backtrack(combination + letter, next_digits[1:])
                
    output = []
    if digits:
        backtrack("", digits)
    return output

print(letterCombinations("23"))