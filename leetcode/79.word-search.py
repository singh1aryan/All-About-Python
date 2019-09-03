'''

79. Word Search: string matrix
        2x2 matrix, search for the word
        vertical, horizontal
        return true if there
        
    [
        ['a','b','a'],
        ['c','d','e'],
        ['a','g','f'],
    ]
Strategy:
    dfs - 
'''

def word_search(board, word):
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if board[i][j]==word[0] and exist(board, word, i,j, 0):
                return True

    return False
            
# DFS algorithm, going deep in the matrix to find the word
def exist(board, word, i, j, k):

    if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or k>=len(word) or word[k]!=board[i][j]:
        # print(1)
        return False
    
    ch = word[k]
    # Does this have to come?
    # Where to print the true statement for recursive functions?
    if ch == word[len(word)-1] and k==len(word)-1:
        return True
    # backtracking - choose, explore and unchoose
    board[i][j] = '-'
    if(exist(board, word, i+1, j, k+1) or exist(board, word, i, j+1, k+1) or exist(board, word, i-1, j, k+1) or exist(board, word, i, j-1, k+1)):
        return True
    board[i][j] = ch


a = [
    ['a','b','a'],
    ['c','d','e'],
    ['a','g','f'],]
print(word_search(a, "abdg"))# true
print(word_search(a, "abdgf"))# true
print(word_search(a, "abd"))# true
print(word_search(a, "abdc"))# true


# Learning points - Recursion, DFS, Backtracking + DFS, How to recursively backtrack?