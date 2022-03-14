from sys import stdin

input = stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]
cctv = [
    [],
    [0],
    [0,2],
    [0,1],
    [0,1,2],
    [0,1,2,3]
]

n,m = map(int, input().split())

cctv_points = []
board = []
now_cctv_num = 7
answer = 9876543210
empty_count = 0
for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(m):
        if 1 <= board[x][y] <= 5:
            cctv_points.append((x,y,board[x][y]))
        elif board[x][y] == 0:
            empty_count += 1

def solv():
    select_cctv(0,[])
    print(answer)

def select_cctv(now,selected):
    if now == len(cctv_points):
        simul(selected)
        return

    for dir in range(4):
        select_cctv(now+1,selected+[dir])

def simul(selected):
    global now_cctv_num, answer
    now_cctv_num += 1

    count = 0
    for idx in range(len(selected)):
        count += insert_cctv(idx, selected[idx])

    answer = min(answer, empty_count-count)
def insert_cctv(idx,dir):
    global board
    x,y,typ = cctv_points[idx]

    count = 0
    for op in cctv[typ]:
        d = (dir+op)%4
        nx,ny = x,y
        while point_validator(nx,ny):
            if board[nx][ny] != now_cctv_num and (board[nx][ny] < 1 or board[nx][ny] > 6):
                count += 1
                board[nx][ny] = now_cctv_num
            nx += dx[d]
            ny += dy[d]

    return count
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == 6:
        return False
    return True

solv()