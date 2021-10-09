from sys import stdin

input = stdin.readline

n,m,r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def solv():
    global n,m
    p = 0
    for _ in range(min(n,m)//2):
        rotate(p,p)
        p += 1
        n -= 2
        m -= 2

    for row in board:
        print(*row)
def rotate(sx,sy):
    global board
    length = (n-1)*2+(m-1)*2
    row = [0]*length
    idx = 0
    for y in range(sy, sy+m-1):
        row[(idx-r)%length] = board[sx][y]
        idx+=1
    for x in range(sx, sx+n-1):
        row[(idx-r)%length] = board[x][sy+m-1]
        idx += 1
    for y in range(sy+m-1, sy,-1):
        row[(idx-r)%length] = board[sx+n-1][y]
        idx += 1
    for x in range(sx+n-1, sx,-1):
        row[(idx-r)%length] = board[x][sy]
        idx+=1

    idx = 0
    for y in range(sy, sy+m-1):
        board[sx][y] = row[idx]
        idx += 1
    for x in range(sx, sx+n-1):
        board[x][sy+m-1] = row[idx]
        idx += 1
    for y in range(sy+m-1, sy,-1):
        board[sx+n-1][y] = row[idx]
        idx += 1
    for x in range(sx+n-1, sx,-1):
        board[x][sy] = row[idx]
        idx += 1
solv()