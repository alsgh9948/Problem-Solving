from collections import deque

dx = [
    [-1,1,0,0],
    [-1,1,-1,1],
    [-1,-2,-2,-1,1,2,2,1]
]
dy = [
    [0,0,-1,1],
    [-1,-1,1,1],
    [-2,-1,1,2,2,1,-1,-2]
]

n = int(input())
board = []
sx=sy=-1
for i in range(n):
    board.append(list(map(int, input().split())))
    if sx == -1:
        for j in range(n):
            if board[i][j] == 1:
                sx,sy = i,j

def bfs():
    q = deque()
    q.appendleft((sx,sy,0,0,2))
    q.appendleft((sx,sy,0,1,2))
    q.appendleft((sx,sy,0,2,2))
    visited = [[[[False,False,False] for _ in range(n*n+1)] for _ in range(n)] for _ in range(n)]
    visited[sx][sy][2][0]=visited[sx][sy][2][1]=visited[sx][sy][2][2]=True
    while q:
        x, y, cnt, now_typ, target = q.pop()
        if target == n*n+1:
            return cnt
        for typ in range(3):
            if visited[x][y][target][typ] or typ == now_typ:
                continue
            q.appendleft((x, y, cnt + 1, typ, target))

        for d in range(len(dx[now_typ])):
            if now_typ < 2:
                nx,ny = x,y
                while True:
                    nx += dx[now_typ][d]
                    ny += dy[now_typ][d]

                    if not point_validator(nx,ny):
                        break

                    if visited[nx][ny][target][now_typ]:
                        continue

                    visited[nx][ny][target][now_typ] = True
                    if target == board[nx][ny]:
                        q.appendleft((nx, ny, cnt+1, now_typ, target+1))
                    else:
                        q.appendleft((nx,ny,cnt+1,now_typ,target))
            else:
                nx = x + dx[now_typ][d]
                ny = y + dy[now_typ][d]

                if not point_validator(nx, ny) or visited[nx][ny][target][now_typ]:
                    continue

                visited[nx][ny][target][now_typ] = True
                if target == board[nx][ny]:
                    q.appendleft((nx, ny, cnt+1, now_typ, target + 1))
                else:
                    q.appendleft((nx, ny, cnt+1, now_typ, target))

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

print(bfs())