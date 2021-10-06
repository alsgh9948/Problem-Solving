from sys import stdin
from collections import deque

input = stdin.readline
dx = [-2,-1, 1, 2, 2, 1,-1,-2]
dy = [ 1, 2, 2, 1,-1,-2,-2,-1]

t = int(input())
board = [[0]*301 for _ in range(301)]
n = 0
def solv():
    global n
    for num in range(1,t+1):
        n = int(input())
        sx,sy = map(int, input().split())
        gx,gy = map(int, input().split())
        print(bfs(sx,sy,gx,gy,num))
def bfs(sx,sy,gx,gy,num):
    global board
    q = deque()

    q.appendleft((sx,sy,0))
    board[sx][sy] = num

    while q:
        x,y,ans = q.pop()

        if x == gx and y == gy:
            return ans

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,num):
                board[nx][ny] = num
                q.appendleft((nx,ny,ans+1))

def point_validator(x,y,num):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] == num:
        return False
    return True

solv()