# You have an array of logs.  Each log is a space delimited string of words.

# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  
# It is guaranteed that each log has at least one word after its identifier.

# Reorder the logs so that all of the letter-logs come before any digit-log.  
# The letter-logs are ordered lexicographically ignoring identifier, with the 
# identifier used in case of ties.  The digit-logs should be put in their original order.

# Return the final order of the logs.
# Example 1:

# Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

def loglist_withoutorder(list):
    l=0
    r=len(list)-1
    while l<=r:
        a = list[l].split(' ')
        b = list[r].split(' ')
        if a[len(a)-1].isdigit() and b[len(b)-1].isalpha():
            # print(list[l], list[r])
            list[l],list[r] = list[r],list[l]
            l+=1
            r-=1
            continue
        elif a[len(a)-1].isdigit():
            r-=1
            continue
        elif b[len(b)-1].isalpha():
            l+=1
            continue
        
    print(list)
        

loglist_withoutorder(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])

def reorderLogFiles(logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            print(id_, rest)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        # print(sorted(logs, key = f))
        return sorted(logs, key = f) 


reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])

def simpleLogFiles(logs):
    letters = []
    digits = []
    for i in logs:
        a = i.split(' ')
        if a[len(a)-1].isalpha():
            letters.append(i)
        else:
            digits.append(i)
    final_logs = []

    for i in letters:
        final_logs.append(i)
    for i in digits:
        final_logs.append(i)
    print(final_logs)

simpleLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])
