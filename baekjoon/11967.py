from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
switch_board = [[0]*(n+1) for _ in range(n+1)]
board = [[-2]*(n+1) for _ in range(n+1)]

switch = [[]]
for _ in range(m):
    a,b,x,y = map(int, input().split())
    if switch_board[a][b] == 0:
        switch_board[a][b] = len(switch)
        switch.append([(x,y)])
    elif switch_board[a][b] > 0:
        switch[switch_board[a][b]].append((x,y))
    board[x][y] = -1

def solv():
    global board
    q = deque([(1,1)])
    board[1][1] = 0

    visited = [[False]*(n+1) for _ in range(n+1)]
    visited[1][1] = True
    cnt = 1
    while q:
        q_len = len(q)
        flag = False
        for _ in range(q_len):
            x,y = q.pop()

            if board[x][y] == -1:
                q.appendleft((x,y))
                continue

            flag = True
            if switch_board[x][y] != 0:
                for a,b in switch[switch_board[x][y]]:
                    if board[a][b] == -1:
                        board[a][b] = 0
                        cnt += 1

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if point_validator(nx,ny,visited):
                    visited[nx][ny] = True
                    q.appendleft((nx,ny))
        if not flag:
            break
    print(cnt)

def point_validator(x,y,visited):
    if x <= 0 or y <= 0 or x > n or y > n:
        return False
    elif visited[x][y]:
        return False
    elif board[x][y] == -2:
        return False
    return True

solv()