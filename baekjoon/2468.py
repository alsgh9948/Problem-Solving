from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

def solv():
    ans = 1
    for _ in range(100):
        if rain():
            cnt = check_safe_area()
            if cnt == 0:
                return ans
            ans = max(ans,cnt)

def rain():
    global board
    flag = False
    for x in range(n):
        for y in range(n):
            board[x][y] -= 1
            if board[x][y] == 0:
                flag = True
    return flag

def check_safe_area():
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] > 0 and not visited[x][y]:
                bfs(x,y,visited)
                cnt += 1
    return cnt
def bfs(sx,sy,visited):
    q = deque()
    q.appendleft((sx,sy))
    visited[sx][sy] = True

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,visited):
                visited[nx][ny] = True
                q.appendleft((nx,ny))

def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif visited[x][y]:
        return
    elif board[x][y] <= 0:
        return False
    return True

print(solv())