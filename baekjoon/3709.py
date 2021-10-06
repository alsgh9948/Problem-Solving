from sys import stdin

input = stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

tc = int(input())

def solv():
    n,r = map(int, input().split())
    board = [[False]*(n+2) for _ in range(n+2)]
    for _ in range(r):
        x,y = map(int, input().split())
        board[x][y] = True

    sx,sy = map(int, input().split())
    simul(sx,sy,board,n)
def simul(sx,sy,board,n):
    d = set_start_direction(sx,sy,n)
    x,y=sx,sy
    visited = [[[False]*4 for _ in range(n+2)] for _ in range(n+2)]

    while True:
        x += dx[d]
        y += dy[d]
        if visited[x][y][d]:
            print(0,0)
            return
        if x == 0 or y == 0 or x == n+1 or y == n+1:
            break
        visited[x][y][d] = True
        if board[x][y]:
            d = (d+1)%4
    print(x,y)
def set_start_direction(sx,sy,n):
    if sx == 0:
        return 2
    elif sx == n+1:
        return 0
    elif sy == 0:
        return 1
    else:
        return 3
for _ in range(tc):
    solv()