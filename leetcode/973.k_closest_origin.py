# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
# (Here, the distance between two points on a plane is the Euclidean distance.)
# You may return the answer in any order.  The answer is guaranteed to be unique 
# (except for the order that it is in.)

# Input: points = [[1,3],[-2,2]], K = 1, Output: [[-2,2]]
import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
            d=[]
            for i in range(0,len(points)):
                d.append((self.dist(points[i]),i))

            d=sorted(d)
            print(d)
            a=[]
            for i in d:
                a.append(points[i[1]])
                K-=1
                if K==0:
                    break
            return a

    def dist(self, arr):
        return math.sqrt(pow(arr[0],2)+pow(arr[1],2))


print(closest([[1,3],[-2,2]], 1))
# class Solution(object):
#     def kClosest(self, points, K):
#         points.sort(key = lambda P: P[0]**2 + P[1]**2)
#         return points[:K]

#     public int dist(int[] point) {
#         return point[0] * point[0] + point[1] * point[1];
#     }