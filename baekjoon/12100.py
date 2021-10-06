from sys import stdin
import copy
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n = int(stdin.readline().strip())
board = [list(map(int,stdin.readline().strip().split())) for _ in range(n)]
temp_board = []
merge_check = []
ans = 0
def select_dir(cnt,dir_list):
    if cnt >= 5:
        simul(dir_list)
        return
    for d in range(4):
        dir_list[cnt] = d
        select_dir(cnt+1,dir_list)

def simul(dir_list):
    global temp_board,merge_check,ans

    temp_board = copy.deepcopy(board)

    for d in dir_list:
        merge_check = [[False] * n for _ in range(n)]
        find_block(d)

    for row in temp_board:
        ans = max(ans,max(row))

def find_block(d):
    if d == 0:
        for i in range(n):
            for j in range(n):
                if temp_board[i][j] != 0:
                    move_block(i,j,d)
    elif d == 1:
        for i in range(n-1, -1,-1):
            for j in range(n):
                if temp_board[i][j] != 0:
                    move_block(i,j,d)
    elif d == 2:
        for j in range(n):
            for i in range(n):
                if temp_board[i][j] != 0:
                    move_block(i,j,d)
    elif d == 3:
        for j in range(n-1,-1,-1):
            for i in range(n):
                if temp_board[i][j] != 0:
                    move_block(i,j,d)

def move_block(x,y,d):
    global merge_check
    merge_flag = False
    now_num = temp_board[x][y]
    temp_board[x][y] = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        point_validate = point_validator(nx,ny,now_num)
        if point_validate in [1,2]:
            break
        elif point_validate == 3:
            if merge_flag:
                break
            temp_board[nx][ny] = 0
            now_num *= 2
            merge_flag = True
        x,y = nx,ny
    temp_board[x][y] = now_num
    merge_check[x][y] = merge_flag
def point_validator(x,y,now_num):
    if x < 0 or y < 0 or x >= n or y >= n:
        return 1
    elif temp_board[x][y] != 0:
        if now_num != temp_board[x][y] or merge_check[x][y]:
            return 2
        else:
            return 3
    return 0

select_dir(0,[-1,-1,-1,-1,-1])

print(ans)