from sys import stdin

dx = [1,0]
dy = [0,1]
input = stdin.readline

n,k = map(int, input().split())
board = [[0]*n for _ in range(n)]
board[0] = list(map(int, input().split()))

def solv():
    answer = 0
    while True:
        add_fish()
        stack_rotate()
        modify_fish_count()
        set_board()

        fold_board()
        modify_fish_count()
        set_board()
        answer += 1
        if max(board[0])-min(board[0]) <= k:
            print(answer)
            return
def add_fish():
    global board
    target = min(board[0])
    for idx in range(n):
        if board[0][idx] == target:
            board[0][idx] += 1

    board[1][1] = board[0][0]
    board[0][0] = 0

def stack_rotate():
    while True:
        step = 0
        length = 0
        max_x = search_max_x()

        flag=False
        for y in range(n):
            if not flag:
                if board[0][y] == 0:
                    step += 1
                else:
                    flag = True
                    if board[1][y] != 0:
                        length = 1
            else:
                if board[1][y] != 0:
                    length += 1
                else:
                    break
        if step > 0:
            renew_board(step,max_x)

        if board[0][length+max_x-1] == 0:
            return
        for x in range(max_x):
            for y in range(length):
                board[length-y][length+x],board[x][y] = board[x][y],0

def renew_board(step,max_x):
    global board
    for y in range(step, n):
        for x in range(max_x):
            board[x][y-step],board[x][y] = board[x][y],0
def set_board():
    global board
    new_row = []
    max_x = search_max_x()

    for y in range(n):
        if board[0][y] == 0:
            break
        for x in range(max_x):
            if board[x][y] == 0:
                break
            new_row.append(board[x][y])

    for x in range(max_x):
        board[x] = [0]*n
    board[0] = new_row

def fold_board():
    length = n//2
    for y in range(length):
        board[1][n-y-1], board[0][y] = board[0][y], 0

    renew_board(length,2)

    length = n//4
    for x in range(2):
        for y in range(length):
            board[3-x][n//2-y-1],board[x][y]=board[x][y],0

    renew_board(length, 4)

def modify_fish_count():
    global board

    tmp = [[0]*n for _ in range(n)]
    for x in range(n):
        if board[x][0] == 0:
            break
        for y in range(n):
            if board[x][y] == 0:
                break
            for dir in range(2):
                nx = x + dx[dir]
                ny = y + dy[dir]

                if point_validator(nx,ny):
                    d = abs(board[x][y]-board[nx][ny])//5
                    if board[x][y] > board[nx][ny]:
                        tmp[x][y] -= d
                        tmp[nx][ny] += d
                    elif board[x][y] < board[nx][ny]:
                        tmp[nx][ny] -= d
                        tmp[x][y] += d

    for x in range(n):
        for y in range(n):
            board[x][y] += tmp[x][y]
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] == 0:
        return False
    return True
def search_max_x():
    for y in range(n):
        if board[0][y] == 0:
            continue
        for x in range(n):
            if board[x][y] == 0:
                return x
    return n
solv()