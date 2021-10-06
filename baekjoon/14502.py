from collections import deque
from itertools import combinations

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().strip().split())

board = [list(map(int,input().strip().split())) for _ in range(n)]
ans = 0
# def insert_wall(x,y,cnt):
#     if cnt == 3:
#         simul()
#         return
#
#     for i in range(x,n):
#         for j in range(y,m):
#             if board[i][j] == 0:
#                 board[i][j] = 1
#                 insert_wall(i,j+1,cnt+1)
#                 board[i][j] = 0
#         y = 0


def simul(walls):
    simul_board = []
    q = deque()

    for i in range(n):
        row = []
        for j in range(m):
            if board[i][j] == 2:
                q.appendleft((i,j))

            row.append(board[i][j])

        simul_board.append(row)

    for x,y in walls:
        simul_board[x][y] = 1
    while q:
        x,y = q.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny,simul_board):
                continue
            simul_board[nx][ny] = 2
            q.appendleft((nx,ny))

    global ans
    ans = max(ans,check_safe_zone(simul_board))

def point_validator(x,y,simul_board):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif simul_board[x][y] != 0:
        return False
    return True

def check_safe_zone(simul_board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if simul_board[i][j] == 0:
                cnt += 1

    return cnt
# insert_wall(0,0,0)


wall_candidate = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            wall_candidate.append((i, j))

for walls in combinations(wall_candidate, 3):
    simul(walls)

print(ans)