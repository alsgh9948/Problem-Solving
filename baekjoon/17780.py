from sys import stdin
from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
input = stdin.readline

n,k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
horse_board = [[[] for _ in range(n)] for _ in range(n)]
horse = []
for _ in range(k):
    x,y,d = map(int, input().split())

    if d == 1:
        d = 1
    elif d == 2:
        d = 3
    elif d == 3:
        d = 0
    else:
        d = 2
    x -= 1
    y -= 1
    horse_board[x][y].append(len(horse))
    horse.append([x,y,d])
def solv():
    global horse
    turn = 1
    while turn <= 1000:
        for idx in range(k):
            x,y,d = horse[idx]
            if horse_board[x][y][0] != idx:
                continue
            nx,ny=move_horse(idx,False)
            if len(horse_board[nx][ny]) >= 4:
                print(turn)
                return
        turn += 1
    print(-1)
def move_horse(idx,flag=False):
    global horse_board,horse
    x,y,d = horse[idx]
    nx = x + dx[d]
    ny = y + dy[d]

    if point_validator(nx, ny):
        nxt_color = board[nx][ny]

        if nxt_color == 0:
            reset_horse_info(x,y,nx,ny)
            horse_board[nx][ny] += horse_board[x][y]
            horse_board[x][y] = []
        elif nxt_color == 1:
            reset_horse_info(x,y,nx,ny)
            horse_board[x][y].reverse()
            horse_board[nx][ny] += horse_board[x][y]
            horse_board[x][y] = []
        elif nxt_color == 2:
            if flag:
                return x,y
            d = (d+2)%4
            horse[idx][2] = d
            return move_horse(idx,True)
    else:
        if flag:
            return x,y
        d = (d+2)%4
        horse[idx][2] = d
        return move_horse(idx,True)
    return nx,ny
def reset_horse_info(x,y,nx,ny):
    global horse
    for idx in horse_board[x][y]:
        horse[idx] = [nx,ny,horse[idx][2]]
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

solv()