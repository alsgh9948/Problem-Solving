from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

tc = int(input())

def solv():
    orders = input().strip()

    x=y=d=0
    start = [x,y]
    end = [x,y]
    for order in orders:
        if order == 'F':
            x += dx[d]
            y += dy[d]
            start[0] = min(start[0],x)
            start[1] = min(start[1],y)

            end[0] = max(end[0],x)
            end[1] = max(end[1],y)
        elif order == 'B':
            x -= dx[d]
            y -= dy[d]
            start[0] = min(start[0],x)
            start[1] = min(start[1],y)

            end[0] = max(end[0],x)
            end[1] = max(end[1],y)
        elif order == 'L':
            d = (d-1)%4
        elif order == 'R':
            d = (d+1)%4
    print(abs((start[0]-end[0])*(start[1]-end[1])))
for _ in range(tc):
    solv()
