# earthproblem
# letsgosomewhere
# Sample Output
# 3
# 2
vowels = ["a","e","i","o","u"]
a=[]
# def longest(str):
#     i=0
#     while i< len(str):
#         v=""
#         b=i
#         while i<len(str) and str[i] not in vowels:
#             v+= str[i]
#             i+=1
#         i-=1
#         a.append((v,i))
#         if str[i] in vowels:
#             i+=1
#     print(a)

# longest("letsgosomewhere")

def longestVowelsOnlySubstring(S):
    temp, aux, vowels = 0, [], set('aeiou')
    # Count the length of each vowel substring
    for c in S + 'z':
        if c in vowels:
            temp += 1
        elif temp:
            aux.append(temp)
            temp = 0
    print(aux, temp)
    # If the first letter is not vowel, you must cut the head
    if S[0] not in vowels: aux = [0] + aux
    # If the last letter is not vowel, you must cut the tail
    if S[-1] not in vowels: aux += [0]
    # Max length = max head + max tail + max middle
    print(aux)
    return aux[0] + aux[-1] + max(aux[1:-1]) if len(aux) >= 3 else sum(aux)


# print(longestVowelsOnlySubstring("letsgosomewhere"))




def maxlen(strings):
    if not strings: return 0
    return max([len(s) for s in strings])


def vowelsonly(s):
    parts = []
    current = []

    for i, char in enumerate(s):
        if char in 'aeiou':
            current.append(char)
        else:
            if current:
                parts.append(''.join(current))
            current = []

    # last remaining
    if current: parts.append(''.join(current))
    print(current, parts)
    best = float('-inf')

    # if vowel substring is at front and end, aaaBBaaaBBaaa
    # we could consider front, 1 middle, end which makes 3 elements
    if len(parts) > 1 and s.startswith(parts[0]) and s.endswith(parts[-1]):
        best = max(best, len(parts[0]) + len(parts[-1]) + maxlen(parts[1:-1]))

    # if vowel substring is at front only, aaaBBaaBBaaaBB,
    # we could consider front, 1 middle which is 2 elements only
    if len(parts) > 1 and s.startswith(parts[0]):
        best = max(best, len(parts[0]) + maxlen(parts[1:]))

    # if vowel substring is at the end, BBaaBBaaa,
    # we could consider 1 middle, end which makes 2 elements only
    if len(parts) > 1 and s.endswith(parts[-1]):
        best = max(best, len(parts[-1]) + maxlen(parts[:-1]))

    # if substring does not happen at front or end, BBaaaBBBaaaaBBB,
    #   we could consider 1 middle only
    best = max(best, maxlen(parts))

    return best

print(vowelsonly('aaabbaaba'), 6)
# print(vowelsonly('aaabbaab'), 5)
# print(vowelsonly('bbaaabbaa'), 5)
# print(vowelsonly('bbaaabbaabbb'), 3)
# print(vowelsonly('ffaoaoeffaaff'), 5)
# print(vowelsonly('aoao'), 4)
# print(vowelsonly('frfr'), 0)