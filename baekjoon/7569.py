from sys import stdin
from collections import deque

input = stdin.readline

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

m,n,h = map(int, input().split())

board = [[[] for _ in range(n)] for _ in range(h)]
tomato = deque()
empty_cnt = 0
for z in range(h):
    for x in range(n):
        board[z][x] =list(map(int, input().split()))
        for y in range(m):
            if board[z][x][y] == 1:
                tomato.appendleft((z,x,y,0))
            elif board[z][x][y] == 0:
                empty_cnt += 1

def solv():
    global tomato,board,empty_cnt
    while tomato:
        z,x,y,t = tomato.pop()

        for d in range(6):
            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nz,nx,ny):
                board[nz][nx][ny] = 1
                empty_cnt -= 1
                if empty_cnt == 0:
                    return t+1
                tomato.appendleft((nz,nx,ny,t+1))
    return -1
def point_validator(z,x,y):
    if z < 0 or x < 0 or y < 0 or z >= h or x >= n or y >= m:
        return False
    elif board[z][x][y] != 0:
        return False
    return True


if empty_cnt == 0:
    print(0)
else:
    print(solv())