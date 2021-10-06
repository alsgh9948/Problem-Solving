from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,-1, 0, 1, 1, 1, 0,-1]
dy = [ 0, 1, 1, 1, 0,-1,-1,-1]
n,mm,k = map(int, input().split())

board = [[[[],[]] for _ in range(n)] for _ in range(n)]
typ = 0
spread_q = deque()

for _ in range(mm):
    r,c,m,s,d = map(int, input().split())
    board[r-1][c-1][0] = [m,s,d,1,False]
    spread_q.appendleft((r-1,c-1))

def solv():
    global typ,spread_q
    for _ in range(k):
        nxt_typ = (typ+1)%2
        move_ball(nxt_typ)
        merge_ball(nxt_typ)
        typ = (typ+1)%2
    ans = 0
    while spread_q:
        x,y = spread_q.pop()
        if board[x][y][typ][2] == -1:
            ans += board[x][y][typ][0]*4
        else:
            ans += board[x][y][typ][0]
    return ans

def move_ball(nxt_typ):
    global board, typ, spread_q
    q_len = len(spread_q)
    for _ in range(q_len):
        x,y = spread_q.pop()
        m,s,d,cnt,flag = board[x][y][typ]

        d_cnt = 1
        if d == -1:
            d_cnt = 4
            if flag:
                d = 1
            else:
                d = 0
        for _ in range(d_cnt):
            nx = x + dx[d]*s
            ny = y + dy[d]*s

            nx,ny = check_point(nx,ny)
            if board[nx][ny][nxt_typ]:
                board[nx][ny][nxt_typ][0] += m
                board[nx][ny][nxt_typ][1] += s

                if not board[nx][ny][nxt_typ][4] and ((board[nx][ny][nxt_typ][2] % 2 == 0 and d%2 == 0) or (board[nx][ny][nxt_typ][2] % 2 == 1 and d%2 == 1)):
                    board[nx][ny][nxt_typ][2] = d
                else:
                    board[nx][ny][nxt_typ][4] = True
                board[nx][ny][nxt_typ][3] += 1
            else:
                spread_q.appendleft((nx, ny))
                board[nx][ny][nxt_typ] = [m,s,d,1,False]
            d += 2
        board[x][y][typ] = []

def merge_ball(nxt_typ):
    global board

    q_len = len(spread_q)
    for _ in range(q_len):
        x,y = spread_q.pop()
        m,s,d,cnt,flag = board[x][y][nxt_typ]
        if cnt == 1:
            spread_q.appendleft((x,y))
        else:
            m //= 5
            if m == 0:
                board[x][y][nxt_typ] = []
                continue
            s = s//cnt
            board[x][y][nxt_typ] = [m,s,-1,cnt,flag]
            spread_q.appendleft((x, y))

def check_point(x,y):
    if x < 0:
        x = abs(x)%n
        x = n-x
    if x >= n:
        x %= n

    if y < 0:
        y = abs(y)%n
        y = n-y
    if y >= n:
        y %= n

    return x,y
print(solv())