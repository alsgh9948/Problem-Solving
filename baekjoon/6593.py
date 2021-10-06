from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]


def solv():
    while True:
        global l,r,c,board
        l,r,c = map(int, input().split())
        if l == r == c == 0:
            return

        sz=sx=sy=-1
        board = []
        for z in range(l):
            board.append([input().strip() for _ in range(r)])
            if sz == -1:
                for x in range(r):
                    for y in range(c):
                        if board[z][x][y] == 'S':
                            sz,sx,sy = z,x,y
                            break
                    if sz != -1:
                        break
            input()
        answer = bfs(sz,sx,sy)
        if answer >= 0:
            print('Escaped in %d minute(s).'%(answer))
        else:
            print('Trapped!')

def bfs(sz,sx,sy):
    visited = [[[False]*c for _ in range(r)]for _ in range(l)]

    visited[sz][sx][sy] = True
    q = deque([(sz,sx,sy,0)])

    while q:
        z,x,y,cnt = q.pop()

        if board[z][x][y] == 'E':
            return cnt
        for d in range(6):
            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nz,nx,ny,visited):

                visited[nz][nx][ny] = True
                q.appendleft((nz,nx,ny,cnt+1))
    return -1
def point_validator(z,x,y,visited):
    if z < 0 or x < 0 or y < 0 or z >= l or x >= r or y >= c:
        return False
    elif board[z][x][y] == '#':
        return False
    elif visited[z][x][y]:
        return False
    return True

solv()