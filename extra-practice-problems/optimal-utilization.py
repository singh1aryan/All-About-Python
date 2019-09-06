# Input:
# a = [[1, 2], [2, 4], [3, 6]]
# b = [[1, 2]]
# target = 7

# Output: [[2, 1]]
def optimal(a, b, target):
    a.sort(key=lambda x: x[1])
    i=0
    diff = float('inf')
    output = []
    for i in range(len(b)):
        index = bsearch(a, target-b[i][1])
        if target - a[index][1] - b[i][1] == diff:
            output.append([a[index][0], b[i][0]])
        elif 0 <= target-a[index][1]-b[i][1] < diff:
            diff = target - a[index][1] - b[i][1]
            output = [[a[index][0], b[i][0]]]
    return output
    # print(a)

def bsearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2 + 1
        if arr[mid][1] == target:
            return mid
        elif arr[mid][1] < target:
            left = mid
        else:
            right = mid - 1
    return right

# a = [[1, 2], [3, 6], [2, 4]]
# b = [[1, 2]]
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10
# target = 7
print(optimal(a, b, target))