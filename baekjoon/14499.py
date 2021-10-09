from sys import stdin

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
n,m,x,y,k = map(int,stdin.readline().strip().split())

board = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]

command_list = list(map(int, stdin.readline().strip().split()))

dice_cul = [0,0,0,0]
dice_row = [0,0,0,0]

def simul():
    global x,y
    for command in command_list:
        nx = x + dx[command]
        ny = y + dy[command]

        if not point_validator(nx,ny):
            continue
        move_dice(command)
        print(dice_cul[1])

        if board[nx][ny] == 0:
            board[nx][ny] = dice_cul[3]
        else:
            dice_cul[3] = dice_row[3] = board[nx][ny]
            board[nx][ny] = 0
        x,y = nx,ny
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True
def move_dice(command):
    global dice_row, dice_cul
    if command == 1:
        dice_row = dice_row[-1:]+dice_row[:-1]
        dice_cul[1] = dice_row[1]
        dice_cul[3] = dice_row[3]
    elif command == 2:
        dice_row = dice_row[1:]+dice_row[:1]
        dice_cul[1] = dice_row[1]
        dice_cul[3] = dice_row[3]
    elif command == 3:
        dice_cul = dice_cul[1:] + dice_cul[:1]
        dice_row[1] = dice_cul[1]
        dice_row[3] = dice_cul[3]
    elif command == 4:
        dice_cul = dice_cul[-1:] + dice_cul[:-1]
        dice_row[1] = dice_cul[1]
        dice_row[3] = dice_cul[3]

simul()