from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

tc = int(input())

board = []
w=h=-1
def init():
    global board,w,h
    w, h = map(int, input().split())
    board = []
    q = deque()
    visited = [[False] * w for _ in range(h)]

    for x in range(h):
        board.append(list(input().strip()))
        for y in range(w):
            if board[x][y] == '@':
                q.appendleft((x,y,0,0))
                visited[x][y] = True
            elif board[x][y] == '*':
                q.append((x,y,0,1))
    return q,visited
def solv():
    for _ in range(tc):
        q,visited = init()
        print(bfs(q,visited))

def bfs(q,visited):
    global board
    while q:
        x,y,cnt,typ = q.pop()

        if typ == 0 and (x == 0 or y == 0 or x == h-1 or y == w-1):
            return cnt+1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if typ == 0 and point_validator(nx,ny,visited):
                visited[nx][ny] = True
                q.appendleft((nx,ny,cnt+1,typ))
            elif typ == 1 and point_validator(nx,ny):
                board[nx][ny] = '*'
                q.appendleft((nx,ny,0,typ))
    return 'IMPOSSIBLE'
def point_validator(x,y,visited=None):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False
    elif visited and visited[x][y]:
        return False
    elif board[x][y] in ['#','*']:
        return False
    return True

solv()