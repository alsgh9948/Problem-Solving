from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,k = map(int, input().split())
shark_board = []

shark_count = 0
smell_board = [[[] for _ in range(n)] for _ in range(n)]
smell_q = deque()
shark_info = [[] for _ in range(m+1)]
for x in range(n):
    shark_board.append(list(map(lambda x:[int(x),0], input().split())))
    for y in range(n):
        if shark_board[x][y][0] != 0:
            shark_num = shark_board[x][y][0]
            shark_count += 1
            smell_board[x][y] = [shark_num,k]
            smell_q.appendleft((x,y))
            shark_info[shark_num] = [x,y,-1]

for idx, dir in zip(range(1,m+1),list(map(int, input().split()))):
    shark_info[idx][2] = dir-1

dir_board = [[]] + [[list(map(lambda x:int(x)-1, input().split())) for _ in range(4)] for _ in range(m)]
def solv():
    t = 0
    while shark_count > 1 and t < 1000:
        t += 1
        move_shark(t)
        renew_smell_board()
    if t == 1000 and shark_count != 1:
        print(-1)
    else:
        print(t)
def move_shark(move_timing):
    global shark_board, shark_count, shark_info, smell_q
    for num in range(1,m+1):
        if not shark_info[num]:
            continue

        x,y,d = shark_info[num]
        shark_board[x][y] = [0,0]
        nx,ny,nd = search_next_location(num)

        target = shark_board[nx][ny]
        if target[1] == move_timing:
            shark_count -= 1
            if target[0] > num:
                shark_board[nx][ny][0] = num
                shark_info[target[0]] = []
                shark_info[num] = [nx,ny,nd]

            else:
                shark_info[num] = []
        else:
            shark_info[num] = [nx,ny,nd]
            shark_board[nx][ny] = [num, move_timing]

    for num in range(1,m+1):
        if not shark_info[num]:
            continue
        x,y,d = shark_info[num]
        if not smell_board[x][y]:
            smell_q.appendleft((x, y))

        smell_board[x][y] = [num,k+1]

def search_next_location(num):
    my_smell = []
    x,y,dir = shark_info[num]
    for d in dir_board[num][dir]:
        nx = x + dx[d]
        ny = y + dy[d]

        if boundary_validator(nx,ny):
            if not smell_board[nx][ny]:
                return nx,ny,d
            elif smell_board[nx][ny][0] == num and not my_smell:
                my_smell = [nx,ny,d]
    return my_smell
def boundary_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

def renew_smell_board():
    global smell_board, smell_q

    q_len = len(smell_q)
    for _ in range(q_len):
        x,y = smell_q.pop()
        # if smell_board[x][y]:?
        smell_board[x][y][1] -= 1
        if smell_board[x][y][1] == 0:
            smell_board[x][y] = []
        else:
            smell_q.appendleft((x,y))

solv()