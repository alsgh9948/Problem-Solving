from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,k = map(int, input().split())
board = [[0]*(m+1) for _ in range(n+1)]

waste = []
for _ in range(k):
    x,y = map(int, input().split())
    board[x][y] = -1
    waste.append((x,y))
def solv():
    global board

    answer = 0
    for sx,sy in waste:
        if board[sx][sy] == -1:
            q = deque([(sx,sy)])
            cnt = 0
            board[sx][sy] = 0
            while q:
                x,y = q.pop()
                cnt += 1

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if point_validator(nx,ny):
                        board[nx][ny] = 0
                        q.appendleft((nx,ny))
            answer = max(answer, cnt)
    print(answer)
def point_validator(x,y):
    if x <= 0 or y <= 0 or x > n or y > m:
        return False
    elif board[x][y] == 0:
        return False
    return True

solv()