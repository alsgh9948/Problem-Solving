from sys import stdin
from collections import deque

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,1,1,-1]

r,c = map(int, stdin.readline().split())

board = [list(map(int, stdin.readline().split())) for _ in range(r)]
dest = [-1]*(r*c)
ans = [[0]*c for _ in range(r)]

def solv():
    for i in range(r):
        for j in range(c):
            num = spread_ball(i,j)
            x = num//c
            y = num%c
            ans[x][y] += 1

    for row in ans:
        print(*row)
def spread_ball(x,y):
    global dest
    min_num = board[x][y]
    min_dir = None
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]

        if not point_validator(nx,ny,board[x][y]):
            continue

        if min_num > board[nx][ny]:
            min_num = board[nx][ny]
            min_dir = (nx,ny)

    if min_dir:
        if dest[min_dir[0]*c+min_dir[1]] == -1:
            dest[x*c+y] = spread_ball(min_dir[0], min_dir[1])
        else:
            dest[x*c+y] = dest[min_dir[0]*c+min_dir[1]]
        return dest[x*c+y]
    else:
        dest[x*c+y] = x*c+y
        return x * c + y
def point_validator(x,y,num):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    elif board[x][y] > num:
        return False
    return True

solv()