from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,0,1,0,-1,-1,1,1]
dy = [0,1,0,-1,-1,1,1,-1]

r,c,k = map(int, input().split())
board = [[[0,0] for _ in range(c)] for _ in range(r)]
targets = []
heaters = []

visited = [[0]*c for _ in range(r)]
visited_num = 0

for x in range(r):
    data = list(map(int, input().split()))
    for y in range(c):
        if 1 <= data[y] <= 4:
            d = 0
            if data[y] == 1:
                d = 1
            elif data[y] == 2:
                d = 3
            elif data[y] == 3:
                d = 0
            else:
                d = 2
            heaters.append((x,y,d))
        elif data[y] == 5:
            targets.append((x,y))

w = int(input())
wall_board = [[[False]*4 for _ in range(c)] for _ in range(r)]

for _ in range(w):
    x,y,t = map(int, input().split())
    x-=1
    y-=1
    if t == 0:
        wall_board[x][y][0] = wall_board[x-1][y][2] = True
    else:
        wall_board[x][y][1] = wall_board[x][y+1][3] = True

def solv():
    t = 0
    while True:
        t += 1
        if t == 101:
            break
        turn_on_heater()
        renew_board()
        renew_side_board()

        if check_board():
            break
    print(t)

def check_board():
    for x,y in targets:
        if board[x][y][0] < k:
            return False
    return True

def turn_on_heater():
    global board,visited,visited_num

    for sx,sy,d in heaters:
        q = deque([(sx,sy)])
        visited_num += 1
        for now in range(5,0,-1):
            q_len = len(q)
            for _ in range(q_len):
                x,y = q.pop()

                if now == 5:
                    ops = [0]
                else:
                    ops = [4,0,5]
                for op in ops:
                    nd = d+op if d+op != 8 else 4
                    nx = x + dx[nd]
                    ny = y + dy[nd]

                    if boundary_validator(nx,ny) and wall_validator(x,y,d,op) and visited[nx][ny] != visited_num:
                        board[nx][ny][0] += now
                        visited[nx][ny] = visited_num
                        q.appendleft((nx,ny))


def renew_board():
    for x in range(r):
        for y in range(c):
            if board[x][y][0] == 0:
                continue
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if boundary_validator(nx,ny) and not wall_board[x][y][d] and board[x][y][0] > board[nx][ny][0]:
                    op = (board[x][y][0]-board[nx][ny][0])//4
                    board[x][y][1] -= op
                    board[nx][ny][1] += op

    for x in range(r):
        for y in range(c):
            board[x][y][0] += board[x][y][1]
            board[x][y][1] = 0

def renew_side_board():
    global board
    for y in range(1,c-1):
        if board[0][y][0] > 0:
            board[0][y][0] -= 1
        if board[r-1][y][0] > 0:
            board[r-1][y][0] -= 1

    for x in range(r):
        if board[x][0][0] > 0:
            board[x][0][0] -= 1
        if board[x][c-1][0] > 0:
            board[x][c-1][0] -= 1

def boundary_validator(x,y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    return True

def wall_validator(x,y,d,op):
    if op == 0:
        if wall_board[x][y][d]:
            return False
    else:
        if op == 4:
            nd = (d-1)%4
        else:
            nd = (d+1)%4
        nx = x+dx[nd]
        ny = y+dy[nd]
        if wall_board[nx][ny][d] or wall_board[x][y][nd]:
            return False
    return True
solv()