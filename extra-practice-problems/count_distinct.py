# Python3 implementation to find count
# of unique pairs whose sum exists in
# given array

# Returns number of pairs in arr[0..n-1]
# with sum equal to ‘sum’
def getPairsCount(arr, n):

    # Store counts of all elements in map m
    # to find pair (arr[i], sum-arr[i])
    # because (arr[i]) + (sum – arr[i]) = sum
    m = dict()
    for i in range(n):
        m[arr[i]] = m.get(arr[i], 0) + 1

        # To remove duplicate items
        # we use result map
        pairs1 = dict()

        count = 0 # Initialize result
        for i in range(n):
            for j in range(i + 1, n):
                l = arr[i] + arr[j]
                tp = (arr[i], arr[j])
                if l in m.keys():
                    if tp not in pairs1.keys():
                        count += 1
                        pairs1[(arr[i], arr[j])] = 1
                        pairs1[(arr[j], arr[i])] = 1

    print(m)
    return count

# Driver Code
arr = [1, 5, 6, 4, -1, 5, 10]
n = len(arr)
print(getPairsCount(arr, n))

# This code is contributed by Mohit Kumar