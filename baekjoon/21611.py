from sys import stdin

input = stdin.readline
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

n,m = map(int, input().split())
origin_board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()) for _ in range(m))

board = [0]*(n*n-1)
idx_board = [[0]*n for _ in range(n)]
answer = 0
explosion_cnt = [0,0,0,0]
def solv():
    set_board()
    for d,s in commands:
        blizzard(d,s)
        pull_board()

        while explosion():
            pull_board()
        renew_board()
    answer = explosion_cnt[1]+2*explosion_cnt[2]+3*explosion_cnt[3]
    print(answer)

def blizzard(d,s):
    global board
    x=y=n//2

    for _ in range(s):
        x += dx[d]
        y += dy[d]
        idx = idx_board[x][y]
        board[idx] = 0

def pull_board():
    cnt = 0
    for now in range(n*n-1):
        if board[now] == 0:
            cnt += 1
        elif cnt > 0:
            board[now-cnt],board[now] = board[now],0

def explosion():
    global board, answer
    before = board[0]
    cnt = 1
    flag = False
    for now in range(1,n*n-1):
        if board[now] == before:
            cnt += 1
        else:
            if cnt >= 4:
                flag = True
                explosion_cnt[before] += cnt
                for idx in range(now-cnt,now):
                    board[idx] = 0
            cnt = 1
            before = board[now]
    if before != 0 and cnt >= 4:
        flag = True
        answer += cnt * before
        for idx in range(n*n-2-cnt, n*n-2):
            board[idx] = 0
    return flag

def renew_board():
    global board
    new_board = [0]*(n*n-1)
    before = board[0]
    cnt = 1
    idx = 0
    for now in range(1,n*n-1):
        if board[now] == 0:
            break
        if board[now] == before:
            cnt += 1
        else:
            new_board[idx] = cnt
            new_board[idx+1] = before
            idx += 2
            if idx >= n*n-1:
                board = new_board
                return
            cnt = 1
            before = board[now]

    if before != 0:
        new_board[idx] = cnt
        new_board[idx+1] = before
    board = new_board

def set_board():
    global board, idx_board

    rotate_cnt = 0
    max_move_cnt = 1
    x=y=n//2
    idx_board[x][y] = -1

    sdx = [0,1,0,-1]
    sdy = [-1,0,1,0]
    d = 0

    idx = 0
    while True:
        for _ in range(max_move_cnt):
            x += sdx[d]
            y += sdy[d]
            idx_board[x][y] = idx
            board[idx] = origin_board[x][y]
            idx += 1
            if (x,y) == (0,0):
                return
        d = (d+1)%4
        rotate_cnt += 1
        if rotate_cnt == 2:
            rotate_cnt = 0
            max_move_cnt += 1

solv()