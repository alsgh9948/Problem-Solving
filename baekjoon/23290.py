from sys import stdin
from itertools import product
input = stdin.readline
fdx = [0,-1,-1,-1,0,1,1,1]
fdy = [-1,-1,0,1,1,1,0,-1]
START = 's'
END = 'e'

sdx = [-1,0,1,0]
sdy = [0,-1,0,1]

m,s = map(int,input().split())
fish_board = [[[[],[]] for _ in range(4)] for _ in range(4)]
smell_board = [[0]*4 for _ in range(4)]

shark_visited = [[0]*4 for _ in range(4)]
visited_num = 0

for _ in range(m):
    x,y,d = map(lambda x:int(x)-1,input().split())
    fish_board[x][y][0].append(d)

sx,sy = map(lambda x:int(x)-1,input().split())

def solv():
    for _ in range(s):
        copy_fish(START)
        move_fish()
        move_shark()
        remove_smell()
        copy_fish(END)

    print_answer()

def print_answer():
    answer = 0
    for x in range(4):
        for y in range(4):
            answer += len(fish_board[x][y][0])
    print(answer)
def copy_fish(typ):
    global fish_board
    for x in range(4):
        for y in range(4):
            if typ == START:
                for d in fish_board[x][y][0]:
                    fish_board[x][y][1].append(d)
            elif typ == END:
                for d in fish_board[x][y][1]:
                    fish_board[x][y][0].append(d)
                fish_board[x][y][1] = []

def move_fish():
    global fish_board
    temp = []
    for x in range(4):
        for y in range(4):
            if fish_board[x][y][0]:
                for d in fish_board[x][y][0]:
                    temp.append(search_dir(x,y,d))
                fish_board[x][y][0] = []

    for x,y,d in temp:
        fish_board[x][y][0].append(d)

def search_dir(x,y,d):
    for _ in range(8):
        nx = x + fdx[d]
        ny = y + fdy[d]
        if point_validator(nx,ny):
            return nx,ny,d
        d = (d-1)%8
    return x,y,d

def move_shark():
    global sx,sy,fish_board,smell_board,shark_visited,visited_num
    max_count = -1
    targets = []
    tx,ty = sx,sy
    for dirs in product(range(4),repeat=3):
        visited_num += 1
        x,y=sx,sy
        count = 0
        temp_target = []
        for d in dirs:
            x += sdx[d]
            y += sdy[d]
            if boundary_validator(x,y):
                if shark_visited[x][y] != visited_num:
                    shark_visited[x][y] = visited_num
                    count += len(fish_board[x][y][0])
                temp_target.append((x,y))
            else:
                break
        else:
            if max_count < count:
                max_count = count
                targets = temp_target
                tx,ty = x,y
    sx,sy = tx,ty
    for x,y in targets:
        if fish_board[x][y][0]:
            smell_board[x][y] = 3
            fish_board[x][y][0] = []

def remove_smell():
    global smell_board
    for x in range(4):
        for y in range(4):
            if smell_board[x][y] > 0:
                smell_board[x][y] -= 1

def boundary_validator(x,y):
    if x < 0 or y < 0 or x >= 4 or y >= 4:
        return False
    return True
def point_validator(x, y):
    if not boundary_validator(x,y):
        return False
    elif smell_board[x][y] != 0:
        return False
    elif (x, y) == (sx, sy):
        return False
    return True
solv()
