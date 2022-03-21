from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solv():
    global w,h,board,trash_num

    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            return
        board = []
        sx, sy = -1, -1
        trash_num = 0
        for x in range(h):
            board.append(list(input().strip()))
            for y in range(w):
                if board[x][y] == '*':
                    board[x][y] = str(trash_num)
                    trash_num += 1
                elif board[x][y] == 'o':
                    sx, sy = x, y

        print(clean(sx,sy))
def clean(sx,sy):
    q = deque([(sx,sy,0,0)])
    visited = [[[False]*2**trash_num for _ in range(w)] for _ in range(h)]
    visited[sx][sy][0] = True

    while q:
        x,y,b,cnt = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                nxt_bit = b
                if board[nx][ny].isdigit():
                    nxt_bit = b|(1<<int(board[nx][ny]))
                    if nxt_bit == 2**trash_num-1:
                        return cnt+1
                if not visited[nx][ny][nxt_bit]:
                    visited[nx][ny][nxt_bit] = True
                    q.appendleft((nx,ny,nxt_bit,cnt+1))
    return -1
def point_validator(x,y):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False
    elif board[x][y] == 'x':
        return False
    return True
solv()