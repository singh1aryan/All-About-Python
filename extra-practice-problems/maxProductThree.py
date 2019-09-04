# [-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.

# Here's a starting point:

def maximum_product_of_three(nums):
    nums = sorted(nums)
    return nums[-1]*nums[-2]*nums[-3]
  # Fill this in.

print(maximum_product_of_three([-4, -4, 2, 8]))
# 128