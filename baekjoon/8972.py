from sys import stdin
from collections import deque

input = stdin.readline
dx = [1,1,1,0,0,0,-1,-1,-1]
dy = [-1,0,1,-1,0,1,-1,0,1]

board = []
q = deque()
r,c = map(int, input().split())
mx=my=0
for x in range(r):
    board.append(list(input().strip()))
    for y in range(c):
        if board[x][y] == '.':
            board[x][y] = 0
        elif board[x][y] == 'I':
            board[x][y] = -1
            mx,my=x,y
        else:
            board[x][y] = 1
            q.appendleft((x,y))
orders = list(map(int, input().strip()))
def solv():
    global board
    for cnt in range(len(orders)):
        order = orders[cnt]-1
        if not move_my(order):
            print('kraj %d'%(cnt+1))
            return

        if not move_mad():
            print('kraj %d'%(cnt+1))
            return

    for x in range(r):
        for y in range(c):
            if board[x][y] == 0:
                print('.',end='')
            elif board[x][y] == -1:
                print('I', end='')
            else:
                print('R',end='')
        print()
def move_my(order):
    global board,mx,my
    board[mx][my] = 0
    mx += dx[order]
    my += dy[order]
    if board[mx][my] > 0:
        return False
    board[mx][my] = -1
    return True

def move_mad():
    global q,board
    q_len = len(q)
    for _ in range(q_len):
        x,y = q.pop()
        nxt_location = (9875643210, 0, 0)
        for d in range(9):
            nx = x + dx[d]
            ny = y + dy[d]
            if point_validator(nx, ny):
                dist = abs(nx - mx) + abs(ny - my)
                if nxt_location[0] > dist:
                    nxt_location = (dist, nx, ny)
        nx,ny = nxt_location[1:]
        if board[nx][ny] == -1:
            return False
        board[x][y] -= 1
        board[nx][ny] += 1
        q.appendleft((nx,ny))
    renew_mad()
    return True

def renew_mad():
    global q,board
    q_len = len(q)
    destory_arduino = []
    for _ in range(q_len):
        x,y = q.pop()
        if board[x][y] > 1:
            destory_arduino.append((x,y))
        else:
            q.appendleft((x,y))
    for x,y in destory_arduino:
        board[x][y] = 0
def point_validator(x,y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    return True
solv()