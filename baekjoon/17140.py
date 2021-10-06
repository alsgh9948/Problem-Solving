r,c,k = map(int, input().split())


board = [[0]*100 for _ in range(100)]

for i in range(3):
    input_list = list(map(int, input().split()))
    for j in range(3):
        board[i][j] = input_list[j]

max_row = 3
max_col = 3

def solv():
    for t in range(1,101):
        if max_row >= max_col:
            row_order()
        else:
            col_order()
        if board[r-1][c-1] == k:
            print(t)
            return
    print(-1)
def row_order():
    global max_col, board
    tmp_max = 0
    for i in range(max_row):
        idx = 0
        tmp_row = []
        for j in range(max_row):
            if board[i][j] == 0:
                continue
            target = board[i][j]
            tmp_row.append([target, 0])
            for k in range(j,max_row):
                if board[i][k] == target:
                    tmp_row[idx][1] += 1
                    board[i][k] = 0
            idx += 1

        tmp_row = sorted(tmp_row,key= lambda x:(x[1],x[0]))
        for k in range(idx):
            board[i][k*2] = tmp_row[k][0]
            board[i][k*2+1] = tmp_row[k][1]
        tmp_max = max(tmp_max,idx*2)
        tmp_max = 100 if tmp_max >= 100 else tmp_max
    max_col = tmp_max

def col_order():
    global max_row, board
    tmp_max = 0
    for j in range(max_col):
        idx = 0
        tmp_col = []
        for i in range(max_col):
            if board[i][j] == 0:
                continue
            target = board[i][j]
            tmp_col.append([target, 0])
            for k in range(i,max_col):
                if board[k][j] == target:
                    tmp_col[idx][1] += 1
                    board[k][j] = 0
            idx += 1
        tmp_col = sorted(tmp_col, key = lambda x:(x[1],x[0]))
        for k in range(idx):
            board[k*2][j] = tmp_col[k][0]
            board[k*2+1][j] = tmp_col[k][1]
        tmp_max = max(tmp_max,idx*2)
        tmp_max = 100 if tmp_max >= 100 else tmp_max
    max_row = tmp_max

if board[r-1][c-1] == k:
    print(0)
else:
    solv()