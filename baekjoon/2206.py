from sys import stdin
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m = map(int, stdin.readline().strip().split())

_map = [list(map(int,stdin.readline().strip())) for _ in range(n)]

def bfs():
    visited = [[[False,False] for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0,1,0,0))
    visited[0][0][0] = True
    while q:
        wall_cnt, cnt, x, y = q.pop()
        if x == n-1 and y == m-1:
            print(cnt)
            return True

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not point_check(nx,ny) or visited[nx][ny][wall_cnt]:
                continue
            if _map[nx][ny] == 0:
                visited[nx][ny][wall_cnt] = True
                q.appendleft((wall_cnt,cnt+1,nx,ny))
            elif wall_cnt == 0:
                visited[nx][ny][1] = True
                q.appendleft((1,cnt+1,nx,ny))
    return False
def point_check(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True
if not bfs():
    print(-1)