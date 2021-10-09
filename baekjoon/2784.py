from itertools import permutations
words = []

for _ in range(6):
    words.append(input())

def solv():
    for word in permutations(words,3):
        used = [False]*6
        board = [w for w in word]
        for w in board:
            word_check(w,used)
        if col_check(board,used):
            for w in board:
                print(w)
            return
    print(0)

def word_check(word,used):
    for idx in range(6):
        if words[idx] == word and not used[idx]:
            used[idx] = True
            return True
    return False
def col_check(board,used):
    for j in range(3):
        word = ''
        for i in range(3):
            word += board[i][j]
        if not word_check(word,used):
            return False
    return True

solv()