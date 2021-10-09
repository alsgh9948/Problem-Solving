from sys import stdin
from collections import deque


dx1 = [-1,0,1]
dy1 = [0,-1,0]

dx2 = [-1,0,1]
dy2 = [0,1,0]

n = int(stdin.readline().strip())

tile = [[0]*(n*2) for _ in range(n)]
tile_num = [[0]*(n*2) for _ in range(n)]

x,y = 0,0
num = 1
for _ in range(n*n-n//2):
    a,b = map(int, stdin.readline().strip().split())

    tile[x][y] = a
    tile[x][y+1] = b

    tile_num[x][y] = tile_num[x][y+1] = num
    num += 1
    y += 2
    if y >= n*2 - 1:
        y = 0
        x += 1
        if x%2 == 1:
            y = 1

last_tile_num = num-1
visited = [0] * (num+1)

def bfs():
    global visited

    q = deque()

    q.appendleft((0,0))
    visited[1] = -1

    max_tile_num = 0
    while q:
        x,y = q.pop()

        x1=x2=y1=y2=-1

        if y%2 == 1:
            if x%2 == 0:
                x1,y1 = x,y
                x2,y2 = x,y+1
            else:
                x2, y2 = x, y
                x1, y1 = x, y-1
        else:
            if x%2 == 0:
                x2,y2 = x,y
                x1,y1 = x,y-1

        now_tile_num = tile_num[x][y]

        max_tile_num = max(now_tile_num, max_tile_num)
        if now_tile_num == last_tile_num:
            return max_tile_num

        for d in range(3):
            nx1 = x1 + dx1[d]
            ny1 = y1 + dy1[d]

            if point_validator(x1,y1, nx1,ny1):
                next_tile_num = tile_num[nx1][ny1]
                visited[next_tile_num] = now_tile_num
                q.appendleft((nx1,ny1))

            nx2 = x2 + dx2[d]
            ny2 = y2 + dy2[d]

            if point_validator(x2, y2, nx2, ny2):
                next_tile_num = tile_num[nx2][ny2]
                visited[next_tile_num] = now_tile_num
                q.appendleft((nx2, ny2))
    return max_tile_num

def point_validator(bx,by, nx,ny):
    if nx < 0 or ny < 0 or nx >= n or ny >= n*2:
        return False
    elif tile[nx][ny] == 0:
        return False
    elif tile[bx][by] != tile[nx][ny]:
        return False
    next_tile_num = tile_num[nx][ny]
    if visited[next_tile_num] != 0:
        return False
    return True

rst = bfs()

path = [rst]

nxt = visited[rst]
print(visited)
# while nxt != -1:
#     path.append(nxt+1)
#     nxt = visited[nxt]
#
# print(len(path))
# print(*reversed(path))