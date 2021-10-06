board = []
pos_list = []

row_check = [[False]*10 for _ in range(9)]
col_check = [[False]*10 for _ in range(9)]
square_check = [[False]*10 for _ in range(9)]

def calc_square_index(x, y):
    return 3*(x//3) + y//3

def set_value(x,y,num,val):
    global board, row_check, col_check, square_check

    square_index = calc_square_index(x, y)

    row_check[x][num] = val
    col_check[y][num] = val
    square_check[square_index][num] = val

    if val:
        board[x][y] = num
    else:
        board[x][y] = 0

for i in range(9):
    board.append(list(map(int,input().strip().split())))
    for j in range(9):
        set_value(i, j, board[i][j], True)
        if board[i][j] == 0:
            pos_list.append((i,j))

def select_num(idx):
    global board, row_check, col_check, square_check
    if idx == len(pos_list):
        for row in board:
            print(*row)
        return True

    x,y = pos_list[idx]
    for num in range(1,10):
        square_index = calc_square_index(x,y)

        if row_check[x][num] or col_check[y][num] or square_check[square_index][num]: continue

        set_value(x,y,num,True)

        if select_num(idx+1):
            return True

        set_value(x,y,num,False)

    return False

select_num(0)