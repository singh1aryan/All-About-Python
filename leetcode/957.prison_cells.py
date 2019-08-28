class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        while N>0:
            cells2=[]
            cells2.append(0)
            for i in range(1,7):
                val = 1 if cells[i-1]==cells[i+1] else 0
                cells2.append(val)
            cells2.append(0)
            cells=cells2
            N=(N-1)%14
            
        return cells


# Points:
#     1. Time out -> N = (N-1)%14
#     2. We can copy the arrays over in python by saying arr1=arr2
