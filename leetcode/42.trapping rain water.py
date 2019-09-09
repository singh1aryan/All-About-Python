# we can only add if there is a bigger tower on the right
# we only come to the left if there is a conflict on the right
# we need a way to stop the right side overflowing


def trap(self, height):
        left = 0
        right = len(height)-1
        ans = 0
        left_max = 0
        right_max = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans


# O(N^2) solution - TLE for one test case
# def trap(self, height):
#         left = 0
#         right = len(height)-1
#         ans = 0
#         left_max = 0
#         right_max = 0
#         for i in range(1, len(height)-1):
#             left_max = max(height[i], max(height[:i]))
#             right_max = max(height[i], max(height[i:]))
#             ans += min(left_max, right_max)-height[i]
#         return ans

