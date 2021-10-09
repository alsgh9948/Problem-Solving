from collections import deque

dx = [-2,-2, 0, 0, 2, 2]
dy = [-1, 1,-2, 2,-1, 1]

n = int(input().strip())
sx,sy,gx,gy = map(int,input().strip().split())

def solv():
    visited = [[False]*(n+1) for _ in range(n+1)]
    q = deque()
    q.appendleft((sx,sy,0))
    visited[sx][sy] = True

    while q:
        x,y,cnt = q.pop()

        if x == gx and y == gy:
            return cnt

        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny,visited):
                continue

            visited[nx][ny] = True
            q.appendleft((nx,ny,cnt+1))

    return -1
def point_validator(x,y,visited):
    if x < 0 or y < 0 or x > n or y > n:
        return False
    elif visited[x][y]:
        return False
    return True

print(solv())