# Basically word search but have to return all the words
# Word search is a dfs based algorithm where you look for the word using search
# Simple dfs - recursive or iterative.

def wordSearch2(words, board):
    list_words = []
    for word in words:
        if(wordSearch(word, board)):
            list_words.append(word)

    return list_words