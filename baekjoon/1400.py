from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def solv():
    global sign,sign_cnt,sx,sy,board,n,m
    while True:
        board = []

        sx = sy = -1
        sign = []
        sign_cnt = 0

        n, m = map(int, input().split())

        if n == m == 0:
            return
        for x in range(n):
            board.append(list(input().strip()))
            for y in range(m):
                if board[x][y] == 'A':
                    sx,sy = x,y
                elif ord('0') <= ord(board[x][y]) <= ord('9'):
                    sign_cnt += 1

        for _ in range(sign_cnt):
            num,typ,a,b = input().strip().split()
            if typ == '-':
                sign.append((int(a),int(b),typ))
            else:
                sign.append((int(b),int(a),typ))
        print(bfs())
        input()
def bfs():
    q = deque()
    visited = [[False]*m for _ in range(n)]

    q.appendleft((0,sx,sy))
    visited[sx][sy] = True

    while q:
        cnt,x,y = q.pop()

        if board[x][y] == 'B':
            return cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,visited):

                if ord('0') <= ord(board[nx][ny]) <= ord('9'):
                    idx = int(board[nx][ny])
                    a,b,typ = sign[idx]

                    remain_time = (cnt+1) % (a+b)

                    if remain_time == 0:
                        remain_time = a+b
                    if typ == '-':
                        if d in [2,3]:
                            if remain_time <= a:
                                visited[nx][ny] = True
                                q.appendleft((cnt+1,nx,ny))
                            else:
                                q.appendleft((cnt+1,x,y))
                        else:
                            if remain_time > a:
                                visited[nx][ny] = True
                                q.appendleft((cnt+1,nx,ny))
                            else:
                                q.appendleft((cnt+1,x,y))
                    else:
                        if d in [0,1]:
                            if remain_time <= a:
                                visited[nx][ny] = True
                                q.appendleft((cnt + 1, nx, ny))
                            else:
                                q.appendleft((cnt+1,x,y))
                        else:
                            if remain_time > a:
                                visited[nx][ny] = True
                                q.appendleft((cnt + 1, nx, ny))
                            else:
                                q.appendleft((cnt+1,x,y))
                else:
                    visited[nx][ny] = True
                    q.appendleft((cnt + 1, nx, ny))
    return 'impossible'
def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == '.':
        return False
    elif visited[x][y]:
        return False
    return True

solv()