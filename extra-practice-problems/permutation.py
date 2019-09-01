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