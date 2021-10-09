from sys import stdin
from collections import deque

input = stdin.readline
m,n = map(int, input().split())
k = int(input())

bus = [[] for _ in range(k+1)]
for _ in range(k):
    bus_info = list(map(int, input().split()))
    sx,sy,gx,gy=bus_info[1:]
    if sx < gx:
        x_op = y_op = 1
    elif sx > gx:
        x_op = y_op = -1
    else:
        x_op = 1
        if sy < gy:
            y_op = 1
        else:
            y_op = -1

    for x in range(sx,gx+x_op,x_op):
        if y_op == 1:
            ssy = 1
            eey = m+1
        else:
            ssy = m
            eey = 1
        if x == sx:
            ssy = sy
        if x == gx:
          eey = gy
        for y in range(ssy,eey+y_op,y_op):
            bus[bus_info[0]].append((x,y))

sx,sy,gx,gy = map(int, input().split())
def solv():
    q = deque()
    visited = [False]*k

    for idx in range(k):
        if (sx,sy) in bus[idx]:
            q.appendleft((idx,1))
            visited[k] = True

    while q:
        num,cnt = q.pop()
        if bus[num][0] == gx and bus[num][1] == gy:
            print(cnt)
            return

