# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

def strstr(haystack, needle):
    a = len(haystack)
    b = len(needle)
    for i in range(0,a-b+1):
        if haystack[i:i+b] == needle:
            return i
    return -1

# print(strstr("hello", "ll"))
print(strstr("a", "a"))
