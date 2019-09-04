# Example 1:

# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.

def maxDistToClosest(seats):
        a=[]
        for i in range(0,len(seats)):
            if seats[i]==1:
                a.append(i)

        b=[]
        for i in range(0,len(seats)):
            if seats[i]==0:
                m=1000
                for k in a:
                    m=min(m,abs(i-k))
                b.append(m)
        print(max(b))
        return max(b)


maxDistToClosest([1,0,0,0,1,0,1])
# passes 75/79 but times out on the last 4. - This is O(N^2) - optimize it
