from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,0,1,0,-1,1,1,-1]
dy = [0,1,0,-1,1,1,-1,-1]

r1,c1 = map(int, input().split())
r2,c2 = map(int, input().split())

def solv():
    visited = [[False]*9 for _ in range(10)]
    visited[r1][c1] = True

    q = deque([(r1,c1,0)])

    while q:
        x,y,cnt = q.pop()
        if x == r2 and c2 == y:
            print(cnt)
            return

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny) and (nx != r2 or ny != c2):
                dd = d + 4
                for _ in range(2):
                    nnx,nny = nx,ny
                    flag = True
                    for c in range(2):
                        nnx = nnx + dx[dd]
                        nny = nny + dy[dd]
                        if not point_validator(nnx,nny) or (c == 0 and nnx == r2 and nny == c2):
                            flag = False
                            break
                    if flag and not visited[nnx][nny]:
                        visited[nnx][nny] = True
                        q.appendleft((nnx,nny,cnt+1))
                    dd = (dd-1)%4+4
    print(-1)

def point_validator(x,y):
    if x < 0 or y < 0 or x >= 10 or y >= 9:
        return False
    return True
solv()