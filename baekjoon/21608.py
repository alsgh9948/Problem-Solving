from sys import stdin

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
board = [[0]*n for _ in range(n)]

infos = {}
for _ in range(n*n):
    info = list(map(int, input().split()))
    infos[info[0]] = info[1:]

def solv():
    for num, like in infos.items():
        insert_num(num,like)
    print(calc_total())
def calc_total():
    total = 0
    for x in range(n):
        for y in range(n):
            num = board[x][y]
            like = infos[num]
            like_cnt = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if boundary_validator(nx, ny) and board[nx][ny] in like:
                    like_cnt += 1
            if like_cnt > 0:
                total += 10**(like_cnt-1)
    return total
def insert_num(num,like):
    global board

    max_like_cnt = -1
    max_empty_cnt = -1
    tx,ty=-1,-1
    for x in range(n):
        for y in range(n):
            tmp_like_cnt = 0
            tmp_empty_cnt = 0
            if board[x][y] == 0:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if boundary_validator(nx,ny):
                        if board[nx][ny] == 0:
                            tmp_empty_cnt += 1
                        elif board[nx][ny] in like:
                            tmp_like_cnt += 1
                if max_like_cnt < tmp_like_cnt:
                    max_like_cnt = tmp_like_cnt
                    max_empty_cnt = tmp_empty_cnt
                    tx,ty = x,y
                elif max_like_cnt == tmp_like_cnt:
                    if max_empty_cnt < tmp_empty_cnt:
                        max_empty_cnt = tmp_empty_cnt
                        tx,ty = x,y
    board[tx][ty] = num

def boundary_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True
solv()
