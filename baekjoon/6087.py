from sys import stdin
from heapq import heappush, heappop

input = stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

m,n = map(int, input().split())

board = []
sx,sy = -1,-1
for x in range(n):
    board.append(list(input().strip()))
    for y in range(m):
        if sx == -1 and board[x][y] == 'C':
            sx,sy = x,y
            board[x][y] = '.'

def solv():
    pq = []
    visited = [[987654321]*m for _ in range(n)]

    for d in range(4):
        nx = sx + dx[d]
        ny = sy + dy[d]

        if point_validator(nx, ny, visited,0):
            heappush(pq,(0,nx,ny,d))
            visited[nx][ny] = 0

    while pq:
        cnt,x,y,d = heappop(pq)

        if board[x][y] == 'C':
            print(cnt)
            return

        for op in [0,1,-1]:
            nd = (d+op)%4

            nx = x + dx[nd]
            ny = y + dy[nd]

            if point_validator(nx,ny,visited,cnt+abs(op)):
                visited[nx][ny] = cnt+abs(op)
                heappush(pq,(cnt+abs(op),nx,ny,nd))

def point_validator(x,y,visited,cnt):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == '*':
        return False
    elif visited[x][y] < cnt:
        return False
    return True

solv()