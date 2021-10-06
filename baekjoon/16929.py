from sys import stdin

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int, stdin.readline().split())
board = [list(stdin.readline()) for _ in range(n)]

def solv():
    visited = [[False]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            visited[x][y] = True
            if check_cycle(x,y,x,y,1,visited):
                print('Yes')
                return
            visited[x][y] = False
    print('No')
def check_cycle(x,y,gx,gy,cnt,visited):
    if cnt >= 4 and x == gx and y == gy:
        return True

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if cnt >= 3 and nx == gx and ny == gy:
            return True

        if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny] or board[x][y] != board[nx][ny]:
            continue

        visited[nx][ny] = True

        if check_cycle(nx,ny,gx,gy,cnt+1,visited):
            return True
        visited[nx][ny] = False

solv()