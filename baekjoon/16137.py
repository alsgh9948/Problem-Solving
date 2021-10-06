from collections import deque

def point_validator(x,y,flag=True):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif flag and board[x][y] == -1:
        return False
    return True


dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,m = map(int,input().strip().split())

board = []
b_list = []

for i in range(n):
    board.append(list(map(int, input().strip().split())))
    for j in range(n):
        if board[i][j] == 0:
            b_list.append((i,j))

for x,y in b_list:
    for d in range(4):

        nx = x + dx[d]
        ny = y + dy[d]

        if not point_validator(nx,ny,False):
            continue

        if board[nx][ny] <= 0:
            nnx1 = x + dx[(d+1)%4]
            nny1 = y + dy[(d+1)%4]

            nnx2 = x + dx[(d+3)%4]
            nny2 = y + dy[(d+3)%4]
            if (point_validator(nnx1,nny1,False) and board[nnx1][nny1] <= 0) or (point_validator(nnx2,nny2,False) and board[nnx2][nny2] <= 0):
                board[x][y] = -1
                break

def bfs():
    ans = 1000000000
    q = deque()
    visited = [[[False, False] for _ in range(n)] for _ in range(n)]

    q.appendleft((0,0,0))
    visited[0][0][0] = visited[0][0][1] = True

    now = 0
    while q:
        q_len = len(q)
        for _ in range(q_len):
            x,y,flag = q.pop()
            if x == n-1 and y == n-1:
                return now
            if board[x][y] != 1:
                if board[x][y] >= 2:
                    if not (now >= board[x][y] and now%board[x][y] == 0):
                        q.appendleft((x,y,flag))
                        continue
                else:
                    if not (now >= m and now%m == 0):
                        q.appendleft((x,y,flag))
                        continue

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if not point_validator(nx,ny):
                    continue

                if board[nx][ny] == 0:
                    if flag == 1 or visited[nx][ny][1]:
                        continue
                    visited[nx][ny][1] = True
                    q.appendleft((nx, ny, 1))
                elif board[nx][ny] >= 2:
                    if board[x][y] != 1 or visited[nx][ny][flag]:
                        continue
                    visited[nx][ny][flag] = True
                    q.appendleft((nx, ny, flag))
                else:
                    if visited[nx][ny][flag]:
                        continue
                    visited[nx][ny][flag] = True
                    q.appendleft((nx, ny, flag))
        now+=1

print(bfs())