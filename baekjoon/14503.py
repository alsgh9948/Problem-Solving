from sys import stdin

input = stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int, input().split())

x,y,d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

def solv():
    global x,y,d
    answer = 1
    visited = [[False]*m for _ in range(n)]
    visited[x][y] = True
    while True:
        flag = False
        for _ in range(4):
            d = (d-1)%4
            nx = x + dx[d]
            ny = y + dy[d]
            if point_validator(nx,ny,visited):
                visited[nx][ny] = True
                answer += 1
                x,y = nx,ny
                flag = True
                break
        if not flag:
            nx = x - dx[d]
            ny = y - dy[d]
            if board[nx][ny] == 0:
                x,y=nx,ny
            else:
                print(answer)
                return
def point_validator(x,y,visited):
    if board[x][y] == 1:
        return False
    elif visited[x][y]:
        return False
    return True
solv()