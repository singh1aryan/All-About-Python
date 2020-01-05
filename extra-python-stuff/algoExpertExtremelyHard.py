def longestIncreasingSubsequence(nums):
	dp = [0]*len(nums)
	for i in range(len(nums)):
		for j in range(0,j):
			if dp[i]==dp[j] and nums[i]>nums[j]:
				dp[i]+=1
	return dp[-1]

def aiportConnections():
	pass