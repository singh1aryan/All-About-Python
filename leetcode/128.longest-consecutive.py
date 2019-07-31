class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set((nums))
        ans = 0
        for i in range(len(nums)):
            if nums[i] not in st:
                continue
            l = r = nums[i]
            st.remove(nums[i])
            while l-1 in st:
                l = l-1
                st.remove(l)
            while r+1 in st:
                r = r+1
                st.remove(r)
            ans = max(r-l+1, ans)
        return ans