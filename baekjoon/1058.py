from sys import stdin

input = stdin.readline

n = int(input())

board = [[0]*n for _ in range(n)]

for x in range(n):
    rel = input().strip()
    for y in range(n):
        if rel[y] == 'N':
            board[x][y] = 0
        else:
            board[x][y] = 1

def solv():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if board[i][j] != 0 or i==j:
                    continue
                elif board[i][k] == 1 and board[j][k] == 1:
                    board[i][j] = board[i][k] + board[k][j]
    answer = 0
    for row in board:
        answer = max(n-row.count(0),answer)

    print(answer)

solv()