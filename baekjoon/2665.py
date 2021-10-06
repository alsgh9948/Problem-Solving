from sys import stdin
from heapq import heappush,heappop

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]

def solv():
    pq = [(0,0,0)]
    visited = [[False]*n for _ in range(n)]
    while pq:
        cnt,x,y = heappop(pq)

        if x == n-1 and y == n-1:
            print(cnt)
            return

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,visited):
                visited[nx][ny] = True

                if board[nx][ny] == 0:
                    heappush(pq,(cnt+1,nx,ny))
                else:
                    heappush(pq,(cnt,nx,ny))

def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif visited[x][y]:
        return False
    return True

solv()