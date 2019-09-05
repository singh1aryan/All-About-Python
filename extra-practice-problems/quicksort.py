# The great Quicksort algorithm
# The key here is to get the pivot - the middle element
# Get a left array - all elements less than pivot
# Get a middle array - all elements same as pivot
# Get a right array - all elements greater than pivot
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    print('pivot', pivot)
    left = [x for x in arr if x < pivot]
    print('left', left)
    middle = [x for x in arr if x == pivot]
    print('middle', middle)
    right = [x for x in arr if x > pivot]
    print('right', right)
    print('arr', arr)
    print('--------------')
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))
# Prints "[1, 1, 2, 3, 6, 8, 10]"