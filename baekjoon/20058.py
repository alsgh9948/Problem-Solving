from sys import stdin
from collections import deque

input = stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**n)]
l_list = list(map(int, input().split()))

def solv():
    for l in l_list:
        if l != 0:
            board_rotate(l)
        if melt_ice() == 0:
            print(0)
            print(0)
            return

    total, cnt = calc_ans()
    print(total)
    print(cnt)
def board_rotate(l):
    for sx in range(0,2**n,2**l):
        for sy in range(0,2**n,2**l):
            rotate(sx,sy,2**l)

def rotate(sx,sy,cnt):
    global board
    tmp = [[0]*cnt for _ in range(cnt)]

    for x in range(sx,sx+cnt):
        for y in range(sy, sy+cnt):
            tmp[x-sx][y-sy] = board[x][y]

    for x in range(cnt):
        for y in range(cnt):
            board[sx+y][sy+cnt-x-1] = tmp[x][y]

def melt_ice():
    global board
    melt_point = []
    ice_cnt = 0
    for x in range(0,2**n):
        for y in range(0,2**n):
            if board[x][y] != 0:
                ice_cnt += 1
                cnt = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if not point_validator(nx, ny):
                        cnt += 1

                if cnt >= 2:
                    melt_point.append((x, y))
    for x,y in melt_point:
        ice_cnt -= 1
        board[x][y] -= 1
    return ice_cnt
def calc_ans():
    global board
    ans_total = 0
    ans_cnt = 0
    for sx in range(0,2**n):
        for sy in range(0,2**n):
            if board[sx][sy] != 0:
                q = deque([(sx,sy)])
                cnt = 1
                ans_total += board[sx][sy]
                board[sx][sy] = 0

                while q:
                    x,y = q.pop()

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if point_validator(nx,ny):
                            q.appendleft((nx,ny))
                            ans_total += board[nx][ny]
                            cnt += 1
                            board[nx][ny] = 0
                ans_cnt = max(cnt, ans_cnt)
    return ans_total,ans_cnt

def point_validator(x,y):
    if x < 0 or y < 0 or x >= 2**n or y >= 2**n:
        return False
    elif board[x][y] == 0:
        return False
    return True

solv()