#  permute a string
# backtracking of it's kind
# we choose a character, remove it from the string, 
# explore more items, unchoose the character, 
# add it back to the string

def permute(s, chosen):
    if len(s)==0:
        print(chosen)
    else:
        for i in range(0,len(s)):
            # choose
            c=s[i]
            chosen += c
            s=s.replace(s[i], "")

            # explore
            permute(s,chosen)

            # un-choose
            s = s[i:] + c + s[:i]
            chosen = chosen[:-1]

permute("abc", "") 