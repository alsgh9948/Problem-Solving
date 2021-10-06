from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
hx,hy = map(int, input().split())
ex,ey = map(int, input().split())

board = [list(input().split()) for _ in range(n)]

def solv():
    q = deque([(hx-1,hy-1,0,0)])
    visited = [[[False,False] for _ in range(m)] for _ in range(n)]
    visited[hx-1][hy-1][0] = True

    while q:
        x,y,status,cnt = q.pop()

        if x == ex-1 and y == ey-1:
            print(cnt)
            return

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                if board[nx][ny] == '1':
                    if status == 0 and not visited[nx][ny][1]:
                        visited[nx][ny][1] = True
                        q.appendleft((nx,ny,1,cnt+1))
                elif not visited[nx][ny][status]:
                    visited[nx][ny][status] = True
                    q.appendleft((nx,ny,status,cnt+1))
    print(-1)
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

solv()