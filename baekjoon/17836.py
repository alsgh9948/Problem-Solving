from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,t = map(int, input().split())

board = [list(input().split()) for _ in range(n)]

def solv():
    q = deque()
    visited = [[False]*m for _ in range(n)]

    q.appendleft((0,0,0))
    visited[0][0] = True
    ans = 987654321
    while q:
        x,y,cnt = q.pop()
        if cnt > t:
            break

        if board[x][y] == '2':
            gram = cnt + abs(x-(n-1)) + abs(y-(m-1))
            if gram > t:
                continue
            ans = min(ans, gram)
            continue

        if x == n-1 and y == m-1:
            ans = min(ans,cnt)
            break

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,visited):
                visited[nx][ny] = True
                q.appendleft((nx,ny,cnt+1))

    return 'Fail' if ans == 987654321 else ans
def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == '1':
        return False
    elif visited[x][y]:
        return False
    return True

print(solv())