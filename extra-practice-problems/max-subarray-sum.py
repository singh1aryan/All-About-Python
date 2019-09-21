def maxSubArrayLen(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_i = 0
        dict = {0:-1} #this means for index -1, the sum is 0
        max_len = 0
        for idx,v in enumerate(nums):
            # print(idx,v)
            sum_i+=v
            if sum_i not in dict:
                dict[sum_i] = idx
            if sum_i-k in dict:
                print(sum_i,idx,dict[sum_i-k])
                max_len=max(max_len, idx-dict[sum_i-k])
            print(dict)
        return max_len

maxSubArrayLen([1,-1,5,-2,3],3)