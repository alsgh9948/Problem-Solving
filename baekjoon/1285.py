from sys import stdin

n = int(input())
board = []
answer = 0
for x in range(n):
    board.append(list(input().strip()))
    for y in  range(n):
        if board[x][y] == 'H':
            board[x][y] = 1
        else:
            board[x][y] = 0
            answer += 1
def solv():

print(board)
