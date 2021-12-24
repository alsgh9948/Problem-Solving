from sys import stdin

input = stdin.readline
r,c = map(int, input().split())

board = [input().strip() for _ in range(r)]

def solv():
    words = set_word()
    words = sorted(words)
    print(words[0])
def set_word():
    words = set()

    for i in range(r):
        word = ''
        for j in range(c):
            if board[i][j] == '#':
                if len(word) >= 2:
                    words.add(word)
                word = ''
            else:
                word += board[i][j]
        if len(word) >= 2:
            words.add(word)

    for j in range(c):
        word = ''
        for i in range(r):
            if board[i][j] == '#':
                if len(word) >= 2:
                    words.add(word)
                word = ''
            else:
                word += board[i][j]
        if len(word) >= 2:
            words.add(word)
    return words

solv()