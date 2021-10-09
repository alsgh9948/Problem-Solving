from sys import stdin

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
def solv():
    global visited
    visited[n-1][m-1] = 1
    ans = dfs(0,0)
    print(0 if ans == -1 else ans)
def dfs(x,y):
    global visited

    num = board[x][y]
    flag = False
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if point_validator(nx,ny,num):
            if visited[nx][ny] != 0:
                visited[x][y] += visited[nx][ny]
            else:
                cnt = dfs(nx,ny)
                if cnt == -1:
                    continue
                else:
                    visited[x][y] += cnt
            flag = True
    if not flag:
        visited[x][y] = -1
    return visited[x][y]
def point_validator(x,y,num):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif visited[x][y] == -1:
        return False
    elif board[x][y] >= num:
        return False
    return True

solv()