def hashmap(nums):
    b = {}
    # simple hashmap in python - dictionary
    for i in nums:
        if i not in b:
            b[i]=1
        else:
            b[i]+=1

    print(b)

hashmap([1,2,3,4,2,3,1])