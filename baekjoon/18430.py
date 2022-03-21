from sys import stdin

input = stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def solv():
    visited = [[False]*m for _ in range(n)]
    print(select(0,0,visited,0))
def select(x,y,visited,total):
    global answer

    if y == m:
        x += 1
        y = 0

    if x == n:
        return total
    result = 0
    if not visited[x][y]:
        visited[x][y] = True
        for d in range(4):
            nx1 = x + dx[d]
            ny1 = y + dy[d]
            nx2 = x + dx[(d+1)%4]
            ny2 = y + dy[(d+1)%4]

            if point_validator(nx1,ny1,nx2,ny2,visited):
                visited[nx1][ny1] = visited[nx2][ny2] = True
                result = max(result, select(x,y+1,visited,total+board[x][y]*2+board[nx1][ny1]+board[nx2][ny2]))
                visited[nx1][ny1] = visited[nx2][ny2] = False
        visited[x][y] = False
    result = max(result,select(x, y + 1, visited, total))
    return result

def point_validator(x1,y1,x2,y2,visited):
    if x1 < 0 or y1 < 0 or x1 >= n or y1 >= m:
        return False
    elif x2 < 0 or y2 < 0 or x2 >= n or y2 >= m:
        return False
    elif visited[x1][y1] or visited[x2][y2]:
        return False
    return True

solv()