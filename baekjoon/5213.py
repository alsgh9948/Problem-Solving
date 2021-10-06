from sys import stdin
from collections import deque

dx = [
    [-1,0,1],
    [-1,0,1]
]
dy = [
    [0,-1,0],
    [0,1,0]
]
n = int(stdin.readline().strip())

tile = [[0]*(n*2) for _ in range(n)]
tile_num = [[0]*(n*2) for _ in range(n)]

num = 1
x,y = 0,0
for _ in range(n*n-n//2):
    a,b = map(int, stdin.readline().strip().split())

    tile[x][y] = a
    tile[x][y+1] = b

    tile_num[x][y] = num
    tile_num[x][y+1] = num

    y+=2
    if y >= (n*2)-1:
        y = 0
        x += 1
        if x%2==1:
            y = 1
    num += 1

visited = [0]*num
visited[1] = -1
def bfs():
    global visited
    q = deque()
    q.appendleft((0,0,0))
    q.appendleft((1,0,1))
    max_tile_num = 1
    while q:
        p,x,y = q.pop()
        now_tile_num = tile_num[x][y]
        max_tile_num = max(now_tile_num, max_tile_num)

        if now_tile_num == num-1:
            return max_tile_num

        np = (p+1)%2
        for d in range(3):
            nx = x + dx[p][d]
            ny = y + dy[p][d]

            if not point_validator(x,y,nx,ny):
                continue

            nxt_tile_num = tile_num[nx][ny]
            visited[nxt_tile_num] = now_tile_num
            q.appendleft((np,nx,ny))
            if p == 0:
                q.appendleft((0, nx, ny-1))
            else:
                q.appendleft((1, nx, ny+1))
    return max_tile_num

def point_validator(bx,by,nx,ny):
    if nx < 0 or ny < 0 or nx >= n or ny >= n*2:
        return False

    nxt_tile_num = tile_num[nx][ny]
    if visited[nxt_tile_num]:
        return False
    if tile[bx][by] != tile[nx][ny]:
        return False
    if tile[nx][ny] == 0:
        return False
    return True

max_tile_num = bfs()
path = [max_tile_num]
nxt = visited[max_tile_num]
while nxt != -1:
    path.append(nxt)
    nxt = visited[nxt]

print(len(path))
print(*reversed(path))