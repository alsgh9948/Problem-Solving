from sys import stdin

input = stdin.readline
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

origin_board = [[0]*4 for _ in range(4)]
origin_fish_info = [[-1,-1,-1] for _ in range(17)]

sx=sy=sd=answer=0
for x in range(4):
    data = list(map(int, input().split()))
    for y in range(4):
        num,d = data[2*y],data[2*y+1]-1
        origin_fish_info[num] = [x,y,d]
        origin_board[x][y] = num
        if (x,y) == (0,0):
            sd,answer = d,num
            origin_fish_info[num] = [-1,-1,-1]
            origin_board[0][0] = -1

def solv():
    simul(sx,sy,sd,answer,origin_board,origin_fish_info)
    print(answer)

def simul(x,y,d,total,temp_board,temp_fish_info):
    global answer
    answer = max(total, answer)

    board = copy_board(temp_board)
    fish_info = copy_fish(temp_fish_info)

    move_fish(board, fish_info)
    nx,ny = x,y
    board[x][y] = 0
    for _ in range(3):
        nx += dx[d]
        ny += dy[d]

        if boundary_validator(nx,ny):
            if board[nx][ny] > 0:

                num = board[nx][ny]
                tx,ty,td = fish_info[num]

                board[nx][ny] = -1
                fish_info[num] = [-1,-1,-1]

                simul(nx,ny,td,total+num,board, fish_info)

                board[nx][ny] = num
                fish_info[num] = [tx,ty,td]

def copy_fish(src):
    new_fish = []
    for fish in src:
        new_fish.append(fish)
    return new_fish

def copy_board(src):
    new_board = []
    for x in range(4):
        row = []
        for y in range(4):
            row.append(src[x][y])
        new_board.append(row)
    return new_board

def move_fish(board,fish_info):
    for now in range(1,17):
        x,y,d = fish_info[now]
        if d != -1:
            nx,ny,nd = search_next_direction(x,y,d,board)
            target = board[nx][ny]
            fish_info[now] = [nx,ny,nd]
            fish_info[target] = [x,y,fish_info[target][2]]

            board[x][y],board[nx][ny] = board[nx][ny],board[x][y]

def search_next_direction(x,y,d,board):
    for _ in range(8):
        nx = x + dx[d]
        ny = y + dy[d]

        if point_validator(nx,ny,board):
            return nx,ny,d
        d = (d + 1) % 8

def boundary_validator(x,y):
    if x < 0 or y < 0 or x >= 4 or y >= 4:
        return False
    return True

def point_validator(x,y,board):
    if not boundary_validator(x,y):
        return False
    elif board[x][y] == -1:
        return False
    return True

solv()