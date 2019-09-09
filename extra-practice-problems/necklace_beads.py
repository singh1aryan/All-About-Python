# Necklace beads question asked in an online interview
# You have 2 arrays of same length, each index in the first corresponds to the beads in second
# They are all connected in a sense

# // you can also use imports, for example:
# import java.util.*;
# import java.util.HashMap; 
# import java.util.Map; 

# // you can write to stdout for debugging purposes, e.g.
# // System.out.println("this is a debug message");

# class Solution {
#     public int solution(int[] A) {
#         // write your code in Java SE 8
#         if(A.length==0){
#             return 0;
#         }
#         // using a hashmap for each element which has a set to other beads
#         // iterating once, with a while loop inside, hashmap eventually has the element with all the beads that could possibly come with it
#         HashMap<Integer, Set> map = new HashMap<>();
#         for(int i=0;i<A.length;i++){
#             Set<Integer> a = new HashSet<>();
#             map.put(i, a);
#         }
#         for(int i=0;i<A.length;i++){
#             Set a = map.get(i);
#             a.add(A[i]);
#             int k=i;
#             while(!a.contains(A[A[k]])){
#                 a.add(A[A[k]]);
#                 k=A[k];
#             }
#             map.put(i, a);
#         }
        
#         int m=0;
#         for(int i=0;i<A.length;i++){
#             if(m < map.get(i).size()){
#                 m = map.get(i).size();
#             }
#         }
        
#         return m;
#     }
# }