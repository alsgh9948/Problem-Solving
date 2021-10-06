from sys import stdin

board = [[False]*10 for _ in range(10)]

n = int(stdin.readline())
ans = 0
def solv():
    for _ in range(n):
        t,x,y = map(int,stdin.readline().split())
        drop_red(t,y)
        drop_blue(t,x)

def drop_red(t,y):
    global board
    for x in range(6,10):
        if t == 1 and board[x][y]:
            board[x-1][y] = True
            remove_block_red(t,[x-1])
            return
        elif t == 2 and (board[x][y] or board[x][y+1]):
            board[x-1][y] = board[x-1][y+1] = True
            remove_block_red(t,[x-1])
            return
        elif t == 3 and board[x][y]:
            board[x-1][y] = board[x-2][y] = True
            remove_block_red(t,[x-1,x-2])
            return
    board[9][y] = True
    target = [9]
    if t == 2:
        board[9][y+1] = True
    elif t == 3:
        board[8][y] = True
        target.append(8)
    remove_block_red(t, target)


def remove_block_red(t,x):
    global board, ans
    if t == 1 or t == 2:
        flag = False
        for y in range(4):
            if not board[x[0]][y]:
                flag = True
                break
        if not flag:
            ans += 1
            drop_red_after_remove(x[0], 1)
    else:
        flag1 = flag2 = False
        for y in range(4):
            if not flag1 and not board[x[0]][y]:
                flag1 = True
            if not flag2 and not board[x[1]][y]:
                flag2 = True

            if flag1 == flag2 == True:
                break

        if not flag1 and not flag2:
            ans += 2
            drop_red_after_remove(x[0], 2)
        else:
            if not flag1:
                ans += 1
                drop_red_after_remove(x[0], 1)
            if not flag2:
                ans += 1
                drop_red_after_remove(x[1], 1)

    check_special_zone('r')

def drop_red_after_remove(sx,step):
    global board
    for x in range(sx,4,-1):
        for y in range(4):
            board[x][y], board[x-step][y] = board[x-step][y], False

def drop_blue(t,x):
    global board
    for y in range(6,10):
        if t == 1 and board[x][y]:
            board[x][y-1] = True
            remove_block_blue(t,[y-1])
            return
        elif t == 2 and board[x][y]:
            board[x][y-1] = board[x][y-2] = True
            remove_block_blue(t,[y-1,y-2])
            return
        elif t == 3 and (board[x][y] or board[x+1][y]):
            board[x][y-1] = board[x+1][y-1] = True
            remove_block_blue(t,[y-1])
            return
    board[x][9] = True
    target = [9]
    if t == 3:
        board[x+1][9] = True
    elif t == 2:
        board[x][8] = True
        target.append(8)
    remove_block_blue(t, target)


def remove_block_blue(t,y):
    global board, ans
    if t == 1 or t == 3:
        flag = False
        for x in range(4):
            if not board[x][y[0]]:
                flag = True
                break
        if not flag:
            ans += 1
            drop_blue_after_remove(y[0], 1)
    else:
        flag1 = flag2 = False
        for x in range(4):
            if not flag1 and not board[x][y[0]]:
                flag1 = True
            if not flag2 and not board[x][y[1]]:
                flag2 = True

            if flag1 == flag2 == True:
                break

        if not flag1 and not flag2:
            ans += 2
            drop_blue_after_remove(y[0], 2)
        else:
            if not flag1:
                ans += 1
                drop_blue_after_remove(y[0], 1)
            if not flag2:
                ans += 1
                drop_blue_after_remove(y[1], 1)

    check_special_zone('b')

def drop_blue_after_remove(sy,step):
    global board
    for y in range(sy,4,-1):
        for x in range(4):
            board[x][y], board[x][y-step] = board[x][y-step], False

def check_special_zone(typ):
    global ans
    if typ == 'r':
        flag1 = flag2 = False
        for y in range(4):
            if not flag1 and board[4][y]:
                flag1 = True
            if not flag2 and board[5][y]:
                flag2 = True

            if flag1 == flag2 == True:
                break

        if flag1 and flag2:
            drop_red_after_remove(9,2)
        elif flag1 or flag2:
            drop_red_after_remove(9,1)

    else:
        flag1 = flag2 = False
        for x in range(4):
            if not flag1 and board[x][4]:
                flag1 = True
            if not flag2 and board[x][5]:
                flag2 = True

            if flag1 == flag2 == True:
                break

        if flag1 and flag2:
            drop_blue_after_remove(9,2)
        elif flag1 or flag2:
            drop_blue_after_remove(9,1)
solv()
print(ans)
cnt = 0
for x in range(10):
    for y in range(10):
        if board[x][y]:
            cnt += 1
print(cnt)
