from sys import stdin
from collections import deque

input = stdin.readline

dir = {
    'N':0,
    'S':2,
    'W':3,
    'E':1
}
dx = [1,0,-1,0]
dy = [0,1,0,-1]

a,b = map(int, input().split())
board = [[0]*a for _ in range(b)]

n,m = map(int, input().split())

robots = [[]]
for idx in range(1,n+1):
    y,x,d = input().split()
    x = int(x)-1
    y = int(y)-1
    robots.append([x,y,dir[d]])
    board[x][y] = idx
ops = []

def solv():
    for _ in range(m):
        idx, op, cnt = input().split()
        idx = int(idx)
        cnt = int(cnt)
        if op == 'F':
            if not move_robot(idx,cnt):
                return
        else:
            rotate_robot(idx,op,cnt)
    print('OK')
def move_robot(idx,cnt):
    global robots
    x,y,d = robots[idx]
    board[x][y] = 0
    for _ in range(cnt):
        x += dx[d]
        y += dy[d]

        if not point_validator(idx,x,y):
            return False
    robots[idx] = [x,y,d]
    board[x][y] = idx
    return True

def rotate_robot(idx,op,cnt):
    global robots

    x,y,d = robots[idx]

    if op == 'L':
        d = d-cnt%4
        if d < 0:
            d = 4+d
    else:
        d = (d+cnt)%4

    robots[idx] = [x,y,d]

def point_validator(idx,x,y):
    if x < 0 or y < 0 or x >= b or y >= a:
        print('Robot %d crashes into the wall'%(idx))
        return False
    elif board[x][y] != 0:
        print('Robot %d crashes into robot %d'%(idx,board[x][y]))
        return False
    return True

solv()