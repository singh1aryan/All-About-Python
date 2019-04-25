'''
6. Zero Matrix

Question : 
    Given a boolean matrix, update it so that if any cell is true, all the cells
    in that row and column are true.

Eg:
    [true,  false, false]      [true,  true,  true ]
    [false, false, false]  ‑>  [true,  false, false]
    [false, false, false]      [true,  false, false]

'''

def zeroMatrix(arr):
    for i in arr:
        for j in arr[i]:
            if j == 'true':
                changeColumn()
                changeRow()
                
def changeColumn():
    ''' change the column to true'''
    return 1

def changeRow():
    ''' change the row to true'''
    return 2
            