# find the longest common prefix for array of strings
# first thing which comes to my mind is TRIE - Strings and prefix stuff

def longest(str):
    a=str[0]
    b=str[1]
    c = min(len(a), len(b))
    i=0
    while i<c:
        if a[i] != b[i]:
            break
        i+=1 

    print(str[0][0:i])

longest(["flower", "flowfrt"])
