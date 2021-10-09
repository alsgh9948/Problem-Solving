from collections import deque

tc =  int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def solv(t):
    global n,m,k,micro,board

    n,m,k = map(int, input().split())
    board = [[[[],[]] for _ in range(n)] for _ in range(n)]
    micro = deque()
    for _ in range(k):
        x,y,cnt,d = map(int, input().split())
        micro.appendleft((x,y))
        board[x][y][0].append((cnt,d-1))
    print('#%d %d'%(t, simul()))
def simul():
    typ = 0
    answer = 0
    for _ in range(m):
        move_micro(typ)
        typ = (typ+1)%2

        answer = renew_board(typ)
    return answer
def move_micro(typ):
    global micro, board

    nxt_typ = (typ+1)%2
    q_len = len(micro)
    for _ in range(q_len):
        x,y = micro.pop()
        cnt,d = board[x][y][typ][0]
        board[x][y][typ] = []

        nx = x + dx[d]
        ny = y + dy[d]

        if not board[nx][ny][nxt_typ]:
            micro.appendleft((nx,ny))
        board[nx][ny][nxt_typ].append((cnt,d))

def renew_board(typ):
    total = 0
    for x,y in micro:
        if x == 0 or y == 0 or x == n-1 or y == n-1:
            cnt, d = board[x][y][typ][0]
            cnt //= 2
            if d >= 2:
                d = (d+1)%2+2
            else:
                d = (d+1)%2
            board[x][y][typ] = [(cnt,d)]
            total += cnt

        elif len(board[x][y][typ]) > 1:
            new_total = 0
            board[x][y][typ].sort(reverse=True)
            d = board[x][y][typ][0][1]
            for cnt,dir in board[x][y][typ]:
                new_total += cnt
            board[x][y][typ] = [(new_total, d)]
            total += new_total
        else:
            cnt, d = board[x][y][typ][0]
            total += cnt
    return total
for t in range(1,tc+1):
    solv(t)