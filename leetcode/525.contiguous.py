def findMaxLength(nums):
        nums = [nums[i] if nums[i]==1 else -1 for i in range(len(nums))]
        print(nums)
        dict = {0:-1}
        m, curr_sum = 0,0
        for i in range(len(nums)):
            curr_sum +=nums[i]
            if curr_sum in dict:
                m = max(m,i - dict[curr_sum])
            else:
                dict[curr_sum]=i
        return m
        
nums = [0,1]
print(findMaxLength(nums))