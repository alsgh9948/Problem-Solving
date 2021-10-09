from sys import stdin

input = stdin.readline
INF = 9876543210

n = int(input())
m = int(input())

board = [[INF]*n for _ in range(n)]
for _ in range(m):
    a,b,w = map(int, input().split())
    board[a-1][b-1] = min(board[a-1][b-1],w)

def solv():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    board[i][j] = 0
                elif board[i][j] > board[i][k] + board[k][j]:
                    board[i][j] = board[i][k] + board[k][j]

    for row in board:
        for w in row:
            if w == INF:
                print(0,end=' ')
            else:
                print(w,end=' ')
        print()

solv()