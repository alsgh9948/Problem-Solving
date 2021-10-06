from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())

a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
b1 = list(map(int, input().split()))
b2 = list(map(int, input().split()))
def solv():
    ans = 987654321
    for order in [('a','b'),('b','a')]:
        path = [[False]*(m+1) for _ in range(n+1)]
        src1 = bfs(order[0],path)
        if set_path(path,src1):
            src2 = bfs(order[1],path)
            if set_path(path,src2):
                ans = min(len(src1)+len(src2)-2,ans)

    if ans == 987654321:
        print('IMPOSSIBLE')
    else:
        print(ans)
def set_path(path,src):
    if not src:
        return False
    for x,y in src:
        if path[x][y]:
            return False
        path[x][y] = True
    return True
def bfs(typ,path_map):
    visited = [[[] for _ in range(m+1)] for _ in range(n+1)]
    if typ == 'a':
        sx, sy = a1
        gx, gy = a2
        visited[b1[0]][b1[1]] = [-1,-1]
        visited[b2[0]][b2[1]] = [-1,-1]
    else:
        sx,sy = b1
        gx,gy = b2
        visited[a1[0]][a1[1]] = [-1,-1]
        visited[a2[0]][a2[1]] = [-1,-1]

    q = deque([(sx,sy)])

    visited[sx][sy] = [-1,-1]

    path = []
    while q:
        x,y = q.pop()

        if x == gx and y == gy:
            nx,ny = visited[x][y]
            while nx != -1:
                path.append((nx,ny))
                nx,ny = visited[nx][ny]
            path.append((gx,gy))
            break
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,visited,path_map):
                visited[nx][ny] = [x,y]
                q.appendleft((nx,ny))
    return path
def point_validator(x,y,visited,path_map):
    if x < 0 or y < 0 or x >= n+1 or y >= m+1:
        return False
    elif visited[x][y]:
        return False
    elif path_map[x][y]:
        return False
    return True

solv()