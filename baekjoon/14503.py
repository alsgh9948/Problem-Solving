from sys import stdin

dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,m = map(int, stdin.readline().strip().split())

sx,sy,sd = map(int, stdin.readline().strip().split())

board = [list(stdin.readline().strip().split()) for _ in range(n)]


def simul(x,y,d):
    cnt = 1
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    while True:
        move_status = False
        for _ in range(4):
            d = 3 if d == 0 else d-1

            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny,visited):
                continue

            move_status = True
            visited[nx][ny] = True
            x,y = nx,ny
            cnt += 1
            break
        if not move_status:
            nx = x - dx[d]
            ny = y - dy[d]
            if back_check(nx,ny):
                x,y = nx,ny
            else:
                return cnt
def back_check(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == '1':
        return False
    return True
def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif visited[x][y]:
        return False
    elif board[x][y] == '1':
        return False
    return True

print(simul(sx,sy,sd))