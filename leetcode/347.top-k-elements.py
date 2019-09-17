def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        b = {}
        for i in nums:
            if i not in b:
                b[i] = 1
            else:
                b[i]+=1
        a=[]
        b= sorted(b.items(), key = lambda kv:(kv[1], kv[0]))
        b=b[::-1]
        print(b)
        for i in b:
            if k>0:
                a.append(i[0])
                k-=1
        return a