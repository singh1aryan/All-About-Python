# Example:
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

# Looks recursive on the first go, loops would take it too far
# Tracking the visitng might help, but a basic strategy of choose explore unchoose looks the case
def letterCombination(num):
    