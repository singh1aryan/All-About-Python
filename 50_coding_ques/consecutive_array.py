'''

5. Consecutive Array

Question : 
    Given an unsorted array, find the length of the longest sequence of
    consecutive numbers in the array.
Eg:
    consecutive([4, 2, 1, 6, 5]) = 3, [4, 5, 6]
    consecutive([5, 5, 3, 1]) = 1, [1], [3], or [5]

Approach: 
    recursive/iterative
    
'''

def consecArray(arr):
    l=0
    maxlist = []
    for i in arr:
        j=i # this is important, as we want another loop here
        while j+1 in arr:
            l+=1
            j+=1
        else:
            maxlist.append(l)
            l=0

    return max(maxlist)+1

print(consecArray([4,2,1,6,5]))# 4,5,6 -- 3
print(consecArray([5,5,3,1]))# 5 -- 1
print(consecArray([1,2,3,4,5]))# 1,2,3,4,5 -- 5
print(consecArray([1,2,4,5,6]))# 4,5,6 -- 3
print(consecArray([1,4,5,7,8]))# 4,5 / 7,8 -- 2

'''
go through the array
increment a local variable if 'i' has consec elements - while loop
store the variable in a list
return the max of that list

Java code:- Using HashSet
    HashSet<Integer> values = new HashSet();
        for (int i : a) {
            values.add(i);
        }
         
        // For each value, check if its the first in a sequence of consecutive 
        // numbers and iterate through to find the length of the consecutive 
        // sequence
        
        int maxLength = 0;
        for (int i : values) {
            // If it is not the leftmost value in the sequence, don't bother
            if (values.contains(i - 1)) continue;
            int length = 0;
                
            // Iterate through sequence
            while (values.contains(i++)) length++;
            maxLength = Math.max(maxLength, length);
        }
            
        return maxLength;
'''