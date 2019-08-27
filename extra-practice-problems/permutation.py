def permute(s, chosen):
    if len(s)==0:
        print(chosen)
    else:
        for i in range(0,len(s)):
            # choose
            chosen += s[i]
            s=s.replace(s[i], "")

            # explore
            permute(s,chosen)

            # un-choose
            s = s[i:] + '' + s[:i]
            chosen = chosen[:-1]

permute("abc", "")