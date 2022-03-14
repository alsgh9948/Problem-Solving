from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

tc = int(input())

def solv():
    global n,m,board,target,cnt_board
    n,m = map(int, input().split())
    target = [(0,0,0)]
    cnt_board = [[[-1,-1,-1] for _ in range(m+2)] for _ in range(n+2)]
    board = [['.']*(m+2)]

    for x in range(1,n+1):
        board.append(['.']+list(input().strip())+['.'])
        for y in range(1,m+1):
            if board[x][y] == '$':
                target.append((x,y,len(target)))
    board.append(['.']*(m+2))

    for sx,sy,idx in target:
        bfs(sx,sy,idx)

    answer = 9876543210
    for x in range(n+2):
        for y in range(m+2):
            if cnt_board[x][y][0] != -1 and cnt_board[x][y][1] != -1 and cnt_board[x][y][2] != -1:
                if board[x][y] == '#':
                    answer = min(answer, sum(cnt_board[x][y])-2)
                else:
                    answer = min(answer, sum(cnt_board[x][y]))
    print(answer)
def bfs(sx,sy,idx):
    global cnt_board

    q = deque([(sx,sy,0)])
    cnt_board[sx][sy][idx] = 0

    while q:
        x,y,cnt = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,idx):
                if board[nx][ny] == '#':
                    cnt_board[nx][ny][idx] = cnt+1
                    q.appendleft((nx,ny,cnt+1))
                else:
                    cnt_board[nx][ny][idx] = cnt
                    q.append((nx, ny, cnt))

def point_validator(x,y,idx):
    if x < 0 or y < 0 or x >= n+2 or y >= m+2:
        return False
    elif board[x][y] == '*':
        return False
    elif cnt_board[x][y][idx] != -1:
        return False
    return True
for _ in range(tc):
    solv()