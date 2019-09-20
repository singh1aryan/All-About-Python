def meeting(start, ends):
    all = [(s,1) for s in start] + [(s,-1) for s in ends]

    all = sorted(all)
    num=0
    largest=0
    print(all)
    for pos, t in all:
        num += t
        if largest < num:
            largest = num
    return largest

print(meeting([1,1,2],[1,2,2]))