# Reverse Only Alphabet Characters in a String

# Example 1: "ab-cd-ef"
# Output : "fe-dc-ba"

# Example 2: "abcd-EF-ga"
# Output: "agFE-dc-ba"

def rev(s):
    a=list(s)
    l=0
    r=len(a)-1
    while l<r:
        if a[l].isalpha() and a[r].isalpha():
            a[l],a[r] = a[r],a[l]
            l+=1
            r-=1
        elif not a[l].isalpha():
            l+=1
        elif not a[r].isalpha():
            r-=1
    return ''.join(a)


print(rev("ab-cd-ef"))
print(rev("abcd-EF-ga"))