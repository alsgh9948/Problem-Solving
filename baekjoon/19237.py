from sys import stdin

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,k = map(int, stdin.readline().split())

shark_cnt = m
sharks = [[-1,-1,-1]] + [[] for _ in range(m)]
shark_board = []
for i in range(n):
    tmp = list(map(int, stdin.readline().split()))
    row = []
    for j in range(n):
        if tmp[j] == 0:
            tmp[j] = 1000
        row.append([tmp[j],1000])
        if tmp[j] != 1000:
            sharks[tmp[j]] = [i,j,-1]
    shark_board.append(row)

start_shark_dir = list(map(int, stdin.readline().split()))
for idx in range(m):
    d = start_shark_dir[idx]
    sharks[idx+1][2] = d-1

smell_board = [[[0,0] for _ in range(n)] for _ in range(n)]
shark_move = [[]]

for _ in range(m):
    move = []
    for _ in range(4):
        tmp = list(map(int,stdin.readline().split()))
        move.append([tmp[0]-1,tmp[1]-1,tmp[2]-1,tmp[3]-1])
    shark_move.append(move)

def solv():
    typ = 0
    for t in range(1,1001):
        spred_smell(t,typ)
        move_shark(t,typ)
        typ = (typ+1)%2
        if shark_cnt == 1:
            return t
    return -1

def spred_smell(t,typ):
    global smell_board
    for x,y,d in sharks:
        if d == -1:
            continue
        shark_num = shark_board[x][y][typ]
        smell_board[x][y] = [t+k,shark_num]

def move_shark(t,typ):
    global shark_cnt,sharks,shark_board

    for x,y,d in sharks:
        if d == -1:
            continue
        shark_num = shark_board[x][y][typ]
        smell = []
        flag = False

        nxt_typ = (typ+1)%2
        for dir in shark_move[shark_num][d]:
            nx = x + dx[dir]
            ny = y + dy[dir]

            if point_validator(nx,ny,shark_num,t):
                if smell_board[nx][ny][0] == 0 or smell_board[nx][ny][0] <= t:
                    shark_board[x][y][typ] = 1000
                    if shark_board[nx][ny][nxt_typ] > shark_num:
                        tmp_shark_num = shark_board[nx][ny][nxt_typ]

                        shark_board[nx][ny][nxt_typ] = shark_num

                        if tmp_shark_num != 1000:
                            sharks[tmp_shark_num][2] = -1
                            shark_cnt -= 1
                        sharks[shark_num] = [nx, ny, dir]
                    else:
                        sharks[shark_num][2] = -1
                        shark_cnt -= 1
                    flag = True
                    break
                elif not smell and smell_board[nx][ny][1] == shark_num:
                    smell = [nx,ny,dir]

        if not flag and smell:
            nx,ny,dir = smell
            sharks[shark_num] = [nx, ny, dir]

            shark_board[x][y][typ] = 1000
            shark_board[nx][ny][nxt_typ] = shark_num
def point_validator(x,y,shark_num,t):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif smell_board[x][y][1] != 0 and smell_board[x][y][1] != shark_num and smell_board[x][y][0] > t:
        return False
    return True

print(solv())