# the kth largest element - using heaps/sorting/lists and more

def findKthLargest(nums, k):
        nums = sorted(nums)
        return nums[len(nums)-k]


# we make a list and keep adding the max from nums
# we keep deleting the max element from nums and keep adding to kmax - a temp list
def largest(nums, k):
    m=0
    kmax = []
    while m<k:
        kmax.append(max(nums))
        nums.remove(max(nums))
        m+=1
    print(kmax)
    return kmax[-1]


print(largest([1,2,3,4,5,6],3))