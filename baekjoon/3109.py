from sys import stdin

input = stdin.readline
dx = [-1,0,1]
dy = [ 1,1,1]

n,m = map(int,input().split())

board = [input() for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def solv():
    global visited
    ans = 0
    for x in range(n):
        if visited[x][0] == 0:
            visited[x][0] = 1
            if dfs(x,0):
                ans += 1
    print(ans)

def dfs(x,y):
    global visited
    if y == m-1:
        return True
    for d in range(3):
        nx = x + dx[d]
        ny = y + dy[d]

        if point_validator(nx,ny):
            visited[nx][ny] = 1
            if dfs(nx,ny):
                return True
    return False
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >=m:
        return False
    elif board[x][y] == 'x':
        return False
    elif visited[x][y] != 0:
        return False
    return True

solv()