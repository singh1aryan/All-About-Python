# we will use the prefix sum thing here
# sum of subarray in the array is sum(i,j) = sum(0,j)-sum(0,i)
import collections
def subarraySumPrefixSum(nums, k):
    prefix_sum = [0]*len(nums)
    for i in range(1,len(nums)):
        prefix_sum[i]=sum(nums[0:i-1])

    print(prefix_sum)

def dictSubarraySum(nums,k):
    dict = collections.defaultdict(int)
    dict[0]=1
    current_sum,count = 0,0
    for i in nums:
        current_sum+=i
        count+=dict[current_sum-k]
        dict[current_sum]+=1
    print(count)
    return count

nums,k = [1,1,1], 2
subarraySumPrefixSum(nums, k)
dictSubarraySum(nums, k)
