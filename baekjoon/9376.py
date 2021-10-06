from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

tc = int(input())
board = []
gate_cnt_board = []
n=m=-1
def solv():
    global board,gate_cnt_board,n,m
    for _ in range(tc):
        n,m = map(int,input().split())

        q = deque()
        board = []
        target = []
        gate_cnt_board = [[[-1,-1,-1] for _ in range(m+2)] for _ in range(n+2)]
        board.append(['.']*(m+2))
        for x in range(1,n+1):
            board.append(['.']+list(input().strip())+['.'])
            for y in range(1,m+1):
                if board[x][y] == '$':
                    target.append((x,y))

        board.append(['.']*(m+2))

        gate_cnt_board[0][0][0] = 0
        q.appendleft((0,0,0))
        bfs(q,0)

        sx,sy = target[0]
        gate_cnt_board[sx][sy][1] = 0
        q.appendleft((sx,sy,0))
        bfs(q,1)

        sx,sy = target[1]
        gate_cnt_board[sx][sy][2] = 0
        q.appendleft((sx,sy,0))
        bfs(q,2)

        ans = 987654321
        for x in range(n+2):
            for y in range(m+2):
                if gate_cnt_board[x][y][0] != -1 and gate_cnt_board[x][y][1] != -1 and gate_cnt_board[x][y][2] != -1:
                    if board[x][y] == '#':
                        ans = min(ans,sum(gate_cnt_board[x][y])-2)
                    else:
                        ans = min(ans,sum(gate_cnt_board[x][y]))
        print(ans)
def bfs(q,num):
    global gate_cnt_board
    while q:
        x,y,cnt = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,num):
                if board[nx][ny] == '#':
                    gate_cnt_board[nx][ny][num] = cnt + 1
                    q.appendleft((nx,ny,cnt+1))
                else:
                    gate_cnt_board[nx][ny][num] = cnt
                    q.append((nx,ny,cnt))
def point_validator(x,y,num):
    if x < 0 or y < 0 or x >= n+2 or y >= m+2:
        return False
    elif board[x][y] == '*':
        return False
    elif gate_cnt_board[x][y][num] != -1:
        return False
    return True

solv()