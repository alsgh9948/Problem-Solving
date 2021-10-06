import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

ans = 0
def solv():
    for x in range(0,n):
        for y in range(0,m):
            visited[x][y] = True
            dfs(x,y,board[x][y],1)
            etc(x,y)
            visited[x][y] = False
    print(ans)
def dfs(x,y, sum, cnt):
    if cnt == 4:
        global ans
        ans = max(ans, sum)
        return
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]:
            continue
        visited[nx][ny] = True
        dfs(nx,ny,sum+board[nx][ny],cnt+1)
        visited[nx][ny] = False

def etc(x,y):
    global ans
    if x-1 >= 0 and y+1 < m and y-1 >= 0:
        ans = max(ans, board[x][y]+board[x-1][y]+board[x][y-1]+board[x][y+1])

    if x+1 < n and y+1 < m and y-1 >= 0:
        ans = max(ans, board[x][y]+board[x+1][y]+board[x][y-1]+board[x][y+1])
    if x-1 >= 0 and x+1 < n and y-1 >= 0:
        ans = max(ans, board[x][y]+board[x+1][y]+board[x-1][y]+board[x][y-1])
    if x-1 >= 0 and x+1 < n and y+1 < m:
        ans = max(ans, board[x][y]+board[x+1][y]+board[x-1][y]+board[x][y+1])
solv()