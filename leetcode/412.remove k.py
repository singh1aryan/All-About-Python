def removeKdigits(num, k):
    a = []
    for i in range(len(num)):
        a.append(num[i:i+k])
    m=0
    for i in a:
        if int(i)>m: m=int(i)
    print(m)
    g = num.index(str(m))
    num = num[0:g]+num[g+k:]
    print(num)

numa = "1432219"
k = 3
removeKdigits(numa,k)