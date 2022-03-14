from sys import stdin
from itertools import permutations

input = stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,m,k = map(int, input().split())
origin_board = [list(map(int, input().split())) for _ in range(n)]
operation = [list(map(int, input().split())) for _ in range(k)]

def solv():
    answer = 98765434210
    for order in permutations(operation, k):
        board = copy_board()
        for r,c,s in order:
            sx,sy = r-1,c-1
            ex,ey = r-1,c-1
            for _ in range(s):
                sx -= 1
                sy -= 1
                ex += 1
                ey += 1
                rotate_board(sx,sy,ex,ey,board)
        for row in board:
            answer = min(answer, sum(row))
    print(answer)
def rotate_board(sx,sy,ex,ey,board):
    tmp = board[sx][sy]
    d = 0

    x,y = sx,sy+1
    while True:
        board[x][y],tmp = tmp, board[x][y]
        x += dx[d]
        y += dy[d]

        if x < sx or y < sy or x > ex or y > ey:
            x -= dx[d]
            y -= dy[d]

            d += 1
            if d == 4:
                break

            x += dx[d]
            y += dy[d]

def copy_board():
    board = []
    for x in range(n):
        row = []
        for y in range(m):
            row.append(origin_board[x][y])
        board.append(row)
    return board
solv()