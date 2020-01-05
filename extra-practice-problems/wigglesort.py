print(4)

# 352164 - 351624
# 123456 - 132465
def wiggle(nums):
	i=1
	if len(nums)==2:
		if nums[0]>nums[1]: 
			nums[0],nums[1] = nums[1], nums[0]
		return nums
	while i<len(nums)-1:
		if nums[i-1]<=nums[i]>=nums[i+1]: 
			i+=2
			continue
		else:
			a = max(nums[i-1], nums[i+1])
			if nums[i-1]==a: 
				nums[i], nums[i-1] = nums[i-1], nums[i]
			else: 
				nums[i], nums[i+1] = nums[i+1], nums[i]
		i+=2
	return nums

# print(wiggle([3,5,2,1,6,4]))
# print(wiggle([1,2,3,4,5,6]))
print(wiggle([1,2]))