from sys import stdin,setrecursionlimit

input = stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def solv():
    visited = [[0]*n for _ in range(n)]
    visited[n-1][n-1] = 1
    ans = dfs(0,0,visited)
    print(0 if ans == -1 else ans)
def dfs(x,y,visited):
    flag = False
    cnt = board[x][y]
    if cnt == 0:
        return -1
    for d in ([1,0],[0,1]):
        nx = x + d[0]*cnt
        ny = y + d[1]*cnt

        if point_validator(nx,ny):
            if visited[nx][ny] > 0:
                visited[x][y] += visited[nx][ny]
                flag = True
            elif visited[nx][ny] == 0:
                tmp = dfs(nx,ny,visited)
                if tmp == -1:
                    continue
                else:
                    visited[x][y] += tmp
                    flag = True

    if not flag:
        visited[x][y] = -1
    return visited[x][y]
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

solv()