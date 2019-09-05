# [-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.

# works for only all positive array
def maximum_product(nums):
    nums = sorted(nums)
    return nums[-1]*nums[-2]*nums[-3]
  # Fill this in.

print(maximum_product([4, 4, 2, 8]))
# 128


def maximum_product_of_three(nums):
    # looks dp on the first go, keep track of sum of 3
    nums = sorted(nums)
    return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])

print(maximum_product_of_three([-4, -4, 2, 8]))
# 128

