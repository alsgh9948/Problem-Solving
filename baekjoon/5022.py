from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(lambda x:int(x)+1, input().split())
points = [tuple(map(int, input().split())) for _ in range(4)]

def solv():
    answer = 9876543210
    for start in [(0,2),(2,0)]:
        board = [[() for _ in range(m)] for _ in range(n)]
        typ = False
        tmp_cnt = 0
        for idx in start:
            target = idx
            no_target = (idx+2)%4

            board,cnt = bfs(target, no_target ,board,typ)
            tmp_cnt += cnt
            typ = not typ
        answer = min(answer, tmp_cnt)
    print(answer if answer <= 9876543210 else "IMPOSSIBLE")

def bfs(target, no_target ,board,typ):
    sx,sy = points[target]
    ex,ey = points[target+1]

    q = deque([(sx,sy,0)])

    board[sx][sy] = (-1,-1)
    rst_cnt = 9876543210
    while q:
        x,y,cnt = q.pop()

        if (x,y) == (ex,ey):
            rst_cnt = cnt
            break
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,board,no_target):
                board[nx][ny] = (x,y)
                q.appendleft((nx,ny,cnt+1))

    if typ:
        return board, rst_cnt
    else:
        return renew_board(board,ex,ey),rst_cnt
def renew_board(board,ex,ey):
    x,y = ex,ey
    new_board = [[() for _ in range(m)] for _ in range(n)]
    while board[x][y] != (-1,-1):
        new_board[x][y] = board[x][y]
        x,y = board[x][y]

    new_board[x][y] = (-1,-1)
    return new_board
def point_validator(x,y,board,no_target):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif (x,y) in [points[no_target], points[no_target+1]]:
        return False
    elif board[x][y]:
        return False
    return True

solv()