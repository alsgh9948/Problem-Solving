from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

tc = int(input())
def solv(t):
    global n, board, worm_holl
    n = int(input())
    board = []
    worm_holl = [[] for _ in range(11)]
    for x in range(n):
        board.append(list(map(int, input().split())))
        for y in range(n):
            if board[x][y] >= 6:
                worm_holl[board[x][y]].append((x,y))
    print('#%d %d'%(t,simul()))
def simul():
    global board
    answer = 0
    for sx in range(n):
        for sy in range(n):
            if board[sx][sy] == 0:
                board[sx][sy] = -2
                for d in range(4):
                    answer = max(answer,move_ball(sx,sy,d))
                board[sx][sy] = 0
    return answer
def move_ball(x,y,d):
    cnt = 0
    while True:
        x += dx[d]
        y += dy[d]

        if x < 0 or y < 0 or x >= n or y >= n:
            d = (d+2)%4
            cnt += 1
        elif 1 <= board[x][y] <= 5:
            d = trans_dir(x,y,d)
            cnt += 1
        elif 6 <= board[x][y] <= 10:
            worm_holl_info = worm_holl[board[x][y]]
            if worm_holl_info[0][0] == x and worm_holl_info[0][1] == y:
                x,y = worm_holl_info[1]
            else:
                x,y = worm_holl_info[0]
        elif board[x][y] < 0:
            return cnt

def trans_dir(x,y,d):
    block_num = board[x][y]

    if block_num == 1:
        if d == 0:
            return 2
        elif d == 1:
            return 3
        elif d == 2:
            return 1
        elif d == 3:
            return 0
    elif block_num == 2:
        if d == 0:
            return 1
        elif d == 1:
            return 3
        elif d == 2:
            return 0
        elif d == 3:
            return 2
    elif block_num == 3:
        if d == 0:
            return 3
        elif d == 1:
            return 2
        elif d == 2:
            return 0
        elif d == 3:
            return 1
    elif block_num == 4:
        if d == 0:
            return 2
        elif d == 1:
            return 0
        elif d == 2:
            return 3
        elif d == 3:
            return 1
    elif block_num == 5:
        return (d+2)%4

for t in range(1,tc+1):
    solv(t)