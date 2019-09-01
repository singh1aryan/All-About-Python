# if the elements of the array are unique
def largest_subarray_unique(a, k):
  first_idx = 0
  for x in range(1, len(a) - k + 1):
    if a[first_idx] < a[x]:
      first_idx = x
  return a[first_idx:first_idx+k]

print(largest_subarray_unique([1,4,3,2,5],4))

def largest_subarray(a,k):
  first_idx = 0
  for x in range(1, len(a) - k + 1):
    for i in range(k):
      if a[first_idx] <= a[x]:
        first_idx = x
        break
      else:
        break
  return a[first_idx:first_idx+k]

print(largest_subarray([1,4,3,3,6,2,5,6],5)) # prints [4,3,3,6,2]
print(largest_subarray([1,1,2],2)) # prints [1,2]