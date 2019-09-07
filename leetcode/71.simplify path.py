# Given an absolute path for a file (Unix-style), simplify it.
#  Or in other words, convert it to the canonical path.
# Example 1:

# Input: "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.
# Example 2:

# Input: "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
# Example 3:

# Input: "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

#  return string
def simplify(path):
    places = [p for p in path.split("/") if p!="." and p!=""]
    print(places)
    stack = []
    for p in places:
        if p == "..":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(p)
    return "/" + "/".join(stack)

print(simplify("/a/../../b/../c//.//"))