from sys import stdin

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,k = map(int, input().split())
board = [[0]*n for _ in range(n)]
board[0] = list(map(int, input().split()))

def solv():
    answer = 0
    while max(board[0])-min(board[0]) > k:
        answer += 1
        add_fish()
        renew_board()
        adjust_fish()
        board_to_line()

        fold_board()
        adjust_fish()
        board_to_line()

        min_fish,max_fish = min(board[0]),max(board[0])
        if max_fish-min_fish <= k:
            break
    print(answer)
def add_fish():
    targets = []
    min_count = 9876543210
    for idx in range(n):
        if board[0][idx] < min_count:
            targets = [idx]
            min_count = board[0][idx]
        elif board[0][idx] == min_count:
            targets.append(idx)

    for idx in targets:
        board[0][idx] += 1

def renew_board():
    global board
    l = 1
    h = 2
    board[1][0] = board[0][0]
    board[0] = board[0][1:]+[0]

    while board[0][l+h-1] != 0:
        for y in range(l):
            tx = l-y
            for x in range(h):
                ty = l+x
                board[tx][ty],board[x][y] = board[x][y],0
        for x in range(n):
            board[x] = board[x][l:]+[0]*l
        l,h = h,l+1

def adjust_fish():
    global board
    targets = []
    for x in range(n):
        for y in range(n):

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if point_validator(x,y,nx,ny):
                    amount = (board[x][y] - board[nx][ny])//5
                    targets.append((x,y,-amount))
                    targets.append((nx,ny,amount))

    for x,y,amount in targets:
        board[x][y] += amount

def board_to_line():
    global board
    line = []
    for y in range(n):
        for x in range(n):
            if board[x][y] == 0:
                break
            line.append(board[x][y])
            board[x][y] = 0

    board[0] = line

def fold_board():
    global board
    first_length = n//2
    for y in range(first_length):
        board[1][first_length+y],board[0][first_length-y-1] = board[0][first_length-y-1],0

    for y in range(n//4):
        board[3][n-1-y],board[0][first_length+y] = board[0][first_length+y],0
        board[2][n-1-y],board[1][first_length+y] = board[1][first_length+y],0


def point_validator(x,y,nx,ny):
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        return False
    elif board[nx][ny] == 0:
        return False
    elif board[x][y] <= board[nx][ny]:
        return False
    return True
solv()