from sys import stdin

input = stdin.readline

n = int(input())
board = [list(map(int, input().split())) for i in range(n)]

def solv():
    global board
    for x in range(1,n):
        for y in range(x+1):
            if y == 0:
                board[x][y] = board[x-1][y]+board[x][y]
            elif y == x:
                board[x][y] = board[x][y]+board[x-1][y-1]
            else:
                board[x][y] += max(board[x-1][y],board[x-1][y-1])
    print(max(board[n-1]))
solv()