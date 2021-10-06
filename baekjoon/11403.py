from sys import stdin

input = stdin.readline
n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

def solv():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if board[i][k] == 1 and board[k][j] == 1:
                    board[i][j] = 1

    for row in board:
        print(*row)

solv()