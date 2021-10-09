from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())

board1 = [list(input().strip().split()) for _ in range(n)]
board2 = [list(input().strip().split()) for _ in range(n)]

def solv():
    for x in range(n):
        for y in range(m):
            if board1[x][y] != board2[x][y]:
                bfs(x,y)
                return check_ans()
    return 'YES'

def bfs(sx,sy):
    global board1
    visited = [[False] * m for _ in range(n)]
    q = deque([(sx,sy)])

    visited[sx][sy] = True
    target = board1[sx][sy]
    num = board2[sx][sy]
    while q:
        x,y = q.pop()
        board1[x][y] = num

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,visited,target):
                visited[nx][ny] = True
                q.appendleft((nx,ny))

def check_ans():
    for x in range(n):
        for y in range(m):
            if board1[x][y] != board2[x][y]:
                return 'NO'
    return 'YES'
def point_validator(x,y,visited,target):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif visited[x][y]:
        return False
    elif board1[x][y] != target:
        return False
    return True
print(solv())