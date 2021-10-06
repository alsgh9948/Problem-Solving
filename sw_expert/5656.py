from itertools import permutations
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

tc = int(input())

def solv(t):
    global n,w,h,board,answer
    n,w,h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]

    answer = 9875643210
    select_y([])
    print('#%d %d'%(t,answer))

def select_y(select):
    global answer
    if len(select) == n:
        answer = min(answer, simul(select))
        return

    for y in range(w):
        select.append(y)
        select_y(select)
        select.pop()

def simul(select):
    tmp_board = copy_board(board, [])
    for y in select:
        x = search_target(y,tmp_board)
        remove_ball(x,y,tmp_board)
        renew_board(tmp_board)

    cnt = 0
    for x in range(h):
        for y in range(w):
            if tmp_board[x][y] != 0:
                cnt += 1
    return cnt

def search_target(y,tmp_board):
    for x in range(h):
        if tmp_board[x][y] > 0:
            return x
    return -1

def remove_ball(x,y,tmp_board):
    remove_points = deque([(x,y,tmp_board[x][y]-1)])

    while remove_points:
        x,y,cnt = remove_points.pop()
        tmp_board[x][y] = 0
        if cnt > 0:
            for d in range(4):
                nx = x
                ny = y
                for _ in range(cnt):
                    nx += dx[d]
                    ny += dy[d]

                    if not point_validator(nx,ny):
                        break
                    if tmp_board[nx][ny] > 1:
                        remove_points.appendleft((nx,ny,tmp_board[nx][ny]-1))
                    tmp_board[nx][ny] = 0

def renew_board(tmp_board):
    for y in range(w):
        step = 0
        for x in range(h-1,-1,-1):
            if tmp_board[x][y] == 0:
                step += 1
            elif step > 0:
                tmp_board[x+step][y], tmp_board[x][y] = tmp_board[x][y],0

def point_validator(x,y):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False
    return True

def copy_board(src,dest):
    for x in range(h):
        row = []
        for y in range(w):
            row.append(src[x][y])
        dest.append(row)
    return dest

for t in range(1,tc+1):
    solv(t)