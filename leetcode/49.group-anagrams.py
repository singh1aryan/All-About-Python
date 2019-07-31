class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ch = []
        d={}
        for i in strs:
            t=tuple(sorted(i))
            print(t)
            d[t]= d.get(t,[])+[i] 
            
        print(d)
        return list(d.values())
            