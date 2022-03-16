from sys import stdin

input = stdin.readline
dx = [0,0,-1,1]
dy = [1,-1,0,0]
W = 0
R = 1
B = 2

n,k = map(int, input().split())

color_board = [list(map(int, input().split())) for _ in range(n)]
horse_board = [[[0]+[-1]*k for _ in range(n)] for _ in range(n)]
horse = []
for idx in range(k):
    x,y,d = map(lambda x:int(x)-1, input().split())
    horse_board[x][y][0] += 1
    cnt = horse_board[x][y][0]
    horse_board[x][y][cnt] = idx
    horse.append([x,y,d,cnt])

def solv():
    for turn in range(1,1001):
        for idx in range(k):
            move_horse(idx)
            if check_answer(idx):
                print(turn)
                return
    else:
        print(-1)

def check_answer(horse_idx):
    x,y,d,idx = horse[horse_idx]
    return horse_board[x][y][0] >= 4
def move_horse(horse_idx,flag=False):
    global horse_board, horse

    x,y,d,idx = horse[horse_idx]
    cnt = horse_board[x][y][0]

    nx = x + dx[d]
    ny = y + dy[d]

    targets = horse_board[x][y][idx:cnt + 1]
    if not boundary_validator(nx,ny) or color_board[nx][ny] == B:
        if flag:
            return
        if d >= 2:
            d = (d+1)%2+2
        else:
            d = (d+1)%2

        horse[horse_idx][2] = d
        move_horse(horse_idx,True)
        return
    elif color_board[nx][ny] == R:
        targets.reverse()
    horse_board[x][y][0] -= len(targets)
    for target in targets:
        horse_board[x][y][horse[target][3]] = -1
        horse_board[nx][ny][0] += 1
        target_idx = horse_board[nx][ny][0]
        horse_board[nx][ny][target_idx] = target
        horse[target][0] = nx
        horse[target][1] = ny
        horse[target][3] = target_idx

    return
def boundary_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

solv()