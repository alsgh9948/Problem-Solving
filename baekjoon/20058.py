from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,q = map(int, input().split())
n = 2**n
board = [list(map(lambda x:[int(x),0], input().split())) for _ in range(n)]
l_list = list(map(int, input().split()))

def solv():
    timing = 0
    for l in l_list:
        next_timing = (timing+1)%2
        length = 2**l

        for sx in range(0,n,length):
            for sy in range(0,n,length):
                rotate(sx,sy,length,timing,next_timing)

        if not renew(timing,next_timing):
            print(0)
            print(0)
            return
        timing = next_timing
    print_answer(timing)
def print_answer(timing):
    total = 0
    max_size = 0
    for x in range(n):
        for y in range(n):
            if board[x][y][timing] != 0:
                t,s = bfs(x,y,timing)
                total += t
                max_size = max(max_size,s)

    print(total)
    print(max_size)

def bfs(sx,sy,timing):
    global board
    total = board[sx][sy][timing]
    max_size = 0
    board[sx][sy][timing] = 0

    q = deque([(sx,sy)])
    while q:
        x,y = q.pop()
        max_size += 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,timing):
                total += board[nx][ny][timing]
                board[nx][ny][timing] = 0
                q.appendleft((nx,ny))

    return total, max_size
def renew(timing,next_timing):
    global board
    flag = False
    for x in range(n):
        for y in range(n):
            if board[x][y][timing] > 0:
                flag = True
                cnt = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if point_validator(nx,ny,timing):
                        cnt += 1
                if cnt <= 2:
                    if board[x][y][next_timing] > 0:
                        board[x][y][next_timing] -= 1
    return flag
def point_validator(x,y,timing):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y][timing] == 0:
        return False
    return True
def rotate(sx,sy,length,timing,next_timing):
    global board
    ex,ey = sx+length,sy+length

    new_board = []
    for y in range(sy,ey):
        row = []
        for x in range(ex-1,sx-1,-1):
            row.append(board[x][y])
        new_board.append(row)

    for x in range(sx,ex):
        for y in range(sy,ey):
            board[x][y] = new_board[x-sx][y-sy]
            board[x][y][next_timing] = board[x][y][timing]

solv()

