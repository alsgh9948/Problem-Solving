from collections import deque
from sys import stdin

dx = [-1,1,0,0]
dy = [0,0,1,-1]

r,c,m = map(int, stdin.readline().split())

shark_info = [[]]
board = [[[0,0] for _ in range(c)] for _ in range(r)]
shark_q = deque()
for idx in range(1,m+1):
    x,y,s,d,z = map(int, stdin.readline().split())
    board[x-1][y-1][0] = idx
    shark_q.append((x-1,y-1))
    if d in [1,2]:
        shark_info.append([s%((r*2)-2),d-1,z])
    else:
        shark_info.append([s%((c*2)-2),d-1,z])

ans = 0
def solv():
    typ = 0
    for y in range(c):
        catch_shark(y,typ)
        move_shark(typ)
        typ = (typ+1)%2
    print(ans)
def catch_shark(y,typ):
    global board, ans
    for x in range(r):
        if board[x][y][typ] != 0:
            shark = board[x][y][typ]
            ans += shark_info[shark][2]
            board[x][y][typ] = 0
            return

def move_shark(typ):
    shark_q_len = len(shark_q)

    for _ in range(shark_q_len):
        x,y = shark_q.pop()
        if board[x][y][typ] == 0:
            continue
        shark = board[x][y][typ]
        nxt_typ = (typ+1)%2
        board[x][y][typ] = 0

        s,d,z = shark_info[shark]

        for _ in range(s):
            x += dx[d]
            y += dy[d]

            if x < 0 or y < 0 or x >= r or y >= c:
                x -= dx[d]
                y -= dy[d]

                if d in [0,1]:
                    d = (d+1)%2
                else:
                    d = (d+1)%2+2

                x += dx[d]
                y += dy[d]


        shark_info[shark][1] = d
        if board[x][y][nxt_typ] != 0:
            tmp_shark = shark_info[board[x][y][nxt_typ]]
            if tmp_shark[2] < z:
                board[x][y][nxt_typ] = shark
        else:
            board[x][y][nxt_typ] = shark
            shark_q.appendleft((x,y))

solv()