# For example:
# [(1, 3), (5, 8), (4, 10), (20, 25)]

# This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

# Solution;
# Sort the intervals array using sorted(), check if we need to merge the interval
# replace the i-1 element and remove the ith element
# else i+=1, we don't want i+=1 in the if condition as we would 
def merge(intervals):
    intervals = sorted(intervals)
    a=[]
    i=1
    while i<len(intervals):
        if intervals[i-1][1] >= intervals[i][0]:
            m = intervals[i-1][1] if intervals[i-1][1]>intervals[i][1] else intervals[i][1]
            intervals[i-1] = (intervals[i-1][0], m)
            intervals.remove(intervals[i])
        else:
            i+=1
    return intervals
        
  
print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
print(merge([(1, 4),(0,2),(3,5)]))
print(merge([(1, 4),(4,5)]))
# [(1, 3), (4, 10), (20, 25)]

# sort the array first, then merge
# (1,3)(4,10)(5,8)(20,25)