# Given an input string, reverse the string word by word.
# Example 1:
# Input: "the sky is blue"
# Output: "blue is sky the"

def reverseWords(s):
    a = s.split(" ")
    print(a)
    return a
    

print(reverseWords("  hello world!  "))