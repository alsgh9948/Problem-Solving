my_board = [list(map(int, input().split())) for _ in range(5)]
mc_board = [list(map(int, input().split())) for _ in range(5)]

def solv():
    global my_board
    count = 0
    bingo_count = 0
    for x in range(5):
        for y in range(5):
            count += 1
            bingo_count += my_board_check(mc_board[x][y])
            if bingo_count >= 3:
                print(count)
                return

def my_board_check(target):
    for x in range(5):
        for y in range(5):
            if my_board[x][y] == target:
                my_board[x][y] = 0
                return bingo_check(x, y)
    return 0

def bingo_check(sx,sy):
    #가로 체크
    bingo = True
    bingo_count = 0
    for y in range(5):
        if my_board[sx][y] != 0:
            bingo = False
            break

    if bingo:
        bingo_count += 1

    #세로 체크
    bingo = True
    for x in range(5):
        if my_board[x][sy] != 0:
            bingo = False
            break

    if bingo:
        bingo_count += 1

    # \ 체크
    bingo = True
    if sx==sy:
        for x in range(5):
            y = x
            if my_board[x][y] != 0:
                bingo = False
                break
        if bingo:
            bingo_count += 1

    #/ 체크
    bingo = True
    if sx+sy == 4:
        for x in range(5):
            y = 4-x
            if my_board[x][y] != 0:
                bingo = False
                break
        if bingo:
            bingo_count += 1

    return bingo_count

solv()