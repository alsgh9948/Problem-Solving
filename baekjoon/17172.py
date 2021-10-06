from sys import stdin
from collections import deque
from itertools import combinations

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 987654321
n,m = map(int, stdin.readline().split())

board = []
empty_cnt = 0
candidates = []
for i in range(n):
    board.append(list(map(int, stdin.readline().split())))
    for j in range(n):
        if board[i][j] == 0:
            empty_cnt += 1
        if board[i][j] == 2:
            candidates.append((i,j))

def solv():
    global ans
    for virus in combinations(candidates,m):
        ret = simul(virus)
        if ret != -1:
            ans = ret
    print(-1 if ans == 987654321 else ans)

def simul(virus):
    q = deque()
    visited = [[False]*n for _ in range(n)]

    for x,y in virus:
        q.appendleft((x,y,0))
        visited[x][y] = True

    cnt = 0
    while q:
        x,y,t = q.pop()
        if t >= ans:
            return -1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,visited):
                visited[nx][ny] = True
                if board[nx][ny] == 0:
                    cnt += 1
                    if cnt == empty_cnt:
                        return t+1
                q.appendleft((nx,ny,t+1))
    return -1
def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] == 1:
        return False
    elif visited[x][y]:
        return False
    return True

if empty_cnt == 0:
    print(0)
else:
    solv()