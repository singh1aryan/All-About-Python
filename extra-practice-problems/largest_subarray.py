# if the elements of the array are unique
def largest_subarray(a, k):
  # store first starting index for a subarray as the largest, since 'a' will always be <= 'k'
  first_idx = 0
  # check indices where a subarray of size k can be made
  for x in range(1, len(a) - k + 1):
    # replace the largest first index if a larger value is found
    if a[first_idx] < a[x]:
      first_idx = x

  # return subarray starting at that largest possible first index with size k
  return a[first_idx:first_idx+k]

print(largest_subarray([1,4,3,2,5],4))