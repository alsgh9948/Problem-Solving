from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,k = map(int, input().split())

board = [[False]*m for _ in range(n)]

def solv():
    ans = []
    for _ in range(k):
        sy,sx,ey,ex = map(int, input().split())
        insert_square(sx,sy,ex,ey)

    for x in range(n):
        for y in range(m):
            if not board[x][y]:
                ans.append(count_area_size(x,y))
    ans.sort()
    print(len(ans))
    print(*ans)

def insert_square(sx,sy,ex,ey):
    global board
    for x in range(sx, ex):
        for y in range(sy, ey):
            board[x][y] = True

def count_area_size(sx,sy):
    global board
    q = deque([(sx,sy)])
    board[sx][sy] = True
    cnt = 0
    while q:
        x,y = q.pop()
        cnt += 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                board[nx][ny] = True
                q.appendleft((nx,ny))
    return cnt
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y]:
        return False
    return True

solv()