from collections import deque
from sys import stdin

dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = 987654321
n,m = map(int, stdin.readline().strip().split())

board = []
wall_list = []

for i in range(n):
    board.append(list(stdin.readline().strip()))
    for j in range(m):
        if board[i][j] == '1':
            wall_list.append((i,j))
            board[i][j] = INF
        else:
            board[i][j] = 0
cnt_list = [0]

def solv():
    global board

    insert_num()

    for x in range(n):
        for y in range(m):
            if board[x][y] == INF:
                board[x][y] = -1
                visited = set()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if not point_validator(nx, ny) or board[nx][ny] == INF or board[nx][ny] < 0:
                        continue

                    num = board[nx][ny]
                    if num in visited:
                        continue

                    visited.add(num)
                    board[x][y] -= cnt_list[num]
    for row in board:
        for digit in row:
            num = 0
            if digit < 0:
                num = (-digit)%10
            print(num,end='')
        print()


def insert_num():
    num = 1
    for i in range(n):
        for j in range(m):
           if board[i][j] == 0:
                bfs(i,j,num)
                num += 1

def bfs(sx,sy,num):
    global board,cnt_list
    q = deque()
    q.appendleft((sx,sy))
    cnt = 1
    board[sx][sy] = num
    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny) or board[nx][ny] != 0:
                continue

            board[nx][ny] = num
            cnt += 1
            q.appendleft((nx,ny))
    cnt_list.append(cnt)

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

solv()