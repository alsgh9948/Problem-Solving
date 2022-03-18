from sys import stdin

input = stdin.readline
rotate_block = lambda x,y: (y,3-x)

n = int(input())
score = 0
def solv():
    green_board = [[False] * 4 for _ in range(6)]
    blue_board = [[False] * 4 for _ in range(6)]

    for _ in range(n):
        t,x1,y1 = map(int, input().split())
        x2,y2=x1,y1
        if t == 2:
            y2 += 1
        elif t == 3:
            x2 += 1

        targets = [(x1,y1),(x2,y2)]
        drop_block(green_board,targets,t)
        check_special(green_board)

        x1,y1 = rotate_block(x1,y1)
        x2,y2 = rotate_block(x2,y2)
        targets = [(x2,y2),(x1,y1)]
        if t == 2:
            t = 3
        elif t == 3:
            t = 2

        drop_block(blue_board,targets,t)
        check_special(blue_board)

    remain_block = 0
    for x in range(6):
        for y in range(4):
            remain_block += 1 if green_board[x][y] else 0
            remain_block += 1 if blue_board[x][y] else 0
    print(score)
    print(remain_block)
def drop_block(board,targets,t):
    start = 0 if t == 2 else 1
    op = 0
    if t == 3:
        op = -1

    x = search_drop_location(start,board,targets)
    for tx,ty in targets:
        board[x][ty] = True
        x += op

    while remove_block(board):
        pass
def remove_block(board,flag=False):
    global score

    delete_count = 0
    delete_target_x = -1

    for x in range(5,1,-1):
        if False not in board[x]:
            delete_target_x = max(delete_target_x,x)
            board[x] = [False]*4
            delete_count += 1

    if not flag:
        score += delete_count
    if delete_count > 0:
        renew_board(board,delete_count,delete_target_x-delete_count)
        return True
    return False
def check_special(board):
    delete_count = 0
    if True in board[1]:
        board[5] = [False]*4
        delete_count += 1
        if True in board[0]:
            board[4] = [False]*4
            delete_count += 1

    if delete_count > 0:
        renew_board(board,delete_count,5-delete_count)
        while remove_block(board):
            pass
def renew_board(board,count,start):
    for x in range(start,-1,-1):
        for y in range(4):
            board[x+count][y],board[x][y] = board[x][y], False

def search_drop_location(start,board,targets):
    for x in range(start,6):
        for tx,ty in targets:
            if board[x][ty]:
                return x-1
    return 5

solv()