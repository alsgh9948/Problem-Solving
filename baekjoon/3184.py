from sys import stdin
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

r,c = map(int, stdin.readline().strip().split())

board = []
o_cnt, v_cnt = 0, 0

for i in range(r):
    str_row = stdin.readline().strip()
    row = []
    for j in range(c):
        if str_row[j] == '.':
            row.append(0)
        elif str_row[j] == '#':
            row.append(1)
        elif str_row[j] == 'v':
            row.append(2)
        elif str_row[j] == 'o':
            row.append(3)
    board.append(row)

def solv():
    num = 4
    for i in range(r):
        for j in range(c):
            if board[i][j] in [0, 2, 3]:
                bfs(i, j, num)
                num += 1
    print(o_cnt, v_cnt)

def bfs(sx,sy,num):
    q = deque()
    tv_cnt = 0
    to_cnt = 0

    q.appendleft((sx,sy))
    now_type = board[sx][sy]
    if now_type == 2:
        tv_cnt += 1
    elif now_type == 3:
        to_cnt += 1

    board[sx][sy] = num

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny):
                continue

            nxt_type = board[nx][ny]
            if nxt_type == 2:
                tv_cnt += 1
            elif nxt_type == 3:
                to_cnt += 1

            board[nx][ny] = num
            q.appendleft((nx,ny))

    global o_cnt,v_cnt
    if tv_cnt >= to_cnt:
        v_cnt += tv_cnt
    else:
        o_cnt += to_cnt

def point_validator(x,y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    elif board[x][y] == 1:
        return False
    elif board[x][y] > 3:
        return False
    return True

solv()