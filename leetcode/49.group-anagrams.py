# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ch = []
#         d={}
#         for i in strs:
#             t=tuple(sorted(i))
#             print(t)
#             d[t]= d.get(t,[])+[i] 
            
#         print(d)
#         return list(d.values())
            

def groupAnagrams(strs):
        a = []
        for i in strs:
            m = ''.join(sorted(i))
            a.append(m)

        b={}
        print(a)
        for i in range(0,len(a)):
            if a[i] not in b:
                b[a[i]] = [strs[i]]
            else:
                b[a[i]].append(strs[i])
        res = []
        for i in b:
            res.append(b[i])
        print(res)
a = ["eat", "tea", "tea", "ate", "nat", "bat"]
groupAnagrams(a)

# What's going on? - 
# we sort the strings, make a dictionary and add all the anagrams
# we compare the original array and the sorted one to add stuff