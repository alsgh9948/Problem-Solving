tc = int(input())

def solv(t):
    global n,step,board

    n,step = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    flag_board = [[0]*n for _ in range(n)]
    flag_num = 1

    answer = check_stair(flag_num,flag_board)

    flag_num += 1
    rotate_board()
    answer += check_stair(flag_num,flag_board)

    print('#%d %d'%(t,answer))
def check_stair(flag_num, flag_board):
    answer = 0
    for x in range(n):
        cnt = 0
        front_flag = False
        target = 0
        for y in range(n):
            if front_flag:
                if board[x][y] == target:
                    cnt += 1
                    flag_board[x][y] = flag_num
                    if cnt == step:
                        front_flag = False
                        cnt = 0
                        target = 0
                else:
                    break

            if not front_flag and y+1 < n:
                sub = board[x][y]-board[x][y+1]
                if sub == 1:
                    front_flag = 1
                    target = board[x][y+1]
                elif sub == -1:
                    target = board[x][y]
                    flag = True
                    for by in range(y-1,y-step,-1):
                        if by < 0 or flag_board[x][by] == flag_num or board[x][by] != target:
                            flag = False
                            break
                    if not flag:
                        break
                    cnt = 0
                    target = 0
                elif abs(sub) > 1:
                    target = -1
                    break
        if target == 0:
            answer += 1
    return answer

def rotate_board():
    global board
    new_board = []

    for y in range(n-1,-1,-1):
        row = []
        for x in range(n):
            row.append(board[x][y])
        new_board.append(row)
    board = new_board
for t in range(1,tc+1):
    solv(t)