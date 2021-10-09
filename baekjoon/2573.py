from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())

ices = deque()
board = []
for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(m):
        if board[x][y] != 0:
            ices.appendleft((x,y))

visited = [[0]*m for _ in range(n)]
ice_cnt = len(ices)

def solv():
    global board
    t = 1
    while True:
        new_water = melt_ice()
        if new_water:
            renew_map(new_water)
            if ice_cnt > 0 and check_ans(t):
                return t

        if ice_cnt <= 2:
            return 0
        t += 1
def melt_ice():
    global board,ices

    new_water = []
    for _ in range(ice_cnt):
        x,y = ices.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                board[x][y] -= 1
                if board[x][y] == 0:
                    board[x][y] = -1
                    new_water.append((x,y))
                    break
        if board[x][y] != -1:
            ices.appendleft((x,y))
    return new_water

def renew_map(new_water):
    global board, ice_cnt
    for x,y in new_water:
        ice_cnt -= 1
        board[x][y] = 0

def check_ans(t):
    global visited
    sx,sy = ices[0]
    cnt = 0

    q = deque()
    q.appendleft((sx,sy))
    visited[sx][sy] = t

    while q:
        x,y = q.pop()
        cnt += 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,visited,t):
                visited[nx][ny] = t
                q.appendleft((nx,ny))

    if cnt != ice_cnt:
        return True
    else:
        return False

def point_validator(x,y,visited=None,t=0):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif not visited and board[x][y] != 0:
        return False
    elif visited:
        if visited[x][y] == t:
            return False
        elif board[x][y] == 0:
            return False
    return True

print(solv())