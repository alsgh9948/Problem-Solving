from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())

board = []

sx=sy=-1
for x in range(n):
    board.append(input())
    if sx == -1:
        for y in range(m):
            if board[x][y] == '0':
                sx,sy = x,y

def solv():
    q = deque([(sx,sy,0,0)])
    visited = [[[False]*64 for _ in range(m)] for _ in range(n)]

    visited[sx][sy][0] = True
    while q:
        x,y,cnt,key = q.pop()
        if board[x][y] == '1':
            print(cnt)
            return

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                if 'a' <= board[nx][ny] <= 'f':
                    key_num = ord(board[nx][ny]) - ord('a')
                    new_key = key | (1<<key_num)
                    if not visited[nx][ny][new_key]:
                        visited[nx][ny][new_key] = True
                        q.appendleft((nx,ny,cnt+1,new_key))
                elif 'A' <= board[nx][ny] <= 'F':
                    door = ord(board[nx][ny]) - ord('A')
                    if not visited[nx][ny][key] and key & (1 << door):
                        visited[nx][ny][key] = True
                        q.appendleft((nx, ny, cnt + 1, key))
                else:
                    if not visited[nx][ny][key]:
                        visited[nx][ny][key] = True
                        q.appendleft((nx,ny,cnt+1,key))
    print(-1)
    return

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == '#':
        return False
    return True

solv()
