from sys import stdin
from collections import deque

input = stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**n)]
arr = list(map(int, input().split()))

def solv():
    for l in arr:
        cnt = 2**l
        for sx in range(0,2**n,cnt):
            for sy in range(0,2**n,cnt):
                rotate(sx,sy,cnt,l)
        renew_map()
    total = 0
    ans = 0
    for sx in range(2**n):
        for sy in range(2**n):
            if board[sx][sy] != 0:
                tmp_total,cnt = check_area(sx,sy)
                total += tmp_total
                ans = max(ans,cnt)
    print(total)
    print(ans)
def rotate(x,y,cnt,l):
    global board
    for c in range(l):
        d = 0
        tmp = board[x][y]
        nx,ny = x+c,y+c
        step = 0
        while True:
            nx += dx[d]
            ny += dy[d]
            board[nx][ny],tmp = tmp,board[nx][ny]
            step += 1
            if step == cnt-1:
                d += 1
                if d == 4:
                    break
                step = 0

def check_area(sx,sy):
    q = deque([(sx,sy)])
    total = board[sx][sy]
    cnt = 1
    board[sx][sy] = 0

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                total += board[nx][ny]
                cnt += 1
                board[nx][ny] = 0
                q.appendleft((nx,ny))

    return total,cnt

def renew_map():
    global board
    targets = []
    for x in range(2**n):
        for y in range(2**n):
            if board[x][y] != 0:
                cnt = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if point_validator(nx, ny):
                        cnt += 1
                if cnt <= 2:
                    targets.append((x,y))

    for x,y in targets:
        board[x][y] -= 1
def point_validator(x,y):
    if x < 0 or y < 0 or x >= 2**n or y >= 2**n:
        return False
    elif board[x][y] == 0:
        return False
    return True
solv()