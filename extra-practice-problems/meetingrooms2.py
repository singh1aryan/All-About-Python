def meeting(start, ends):
    all = [(s,1) for s in start] + [(s,-1) for s in ends]

    all = sorted(all)
    print(all)
    num=0
    largest=0
    for pos, t in all:
        num += t
        if largest < num:
            largest = num
            print(largest)
    
    return largest

meeting([1,2,6,5,3],[5,5,7,6,8])