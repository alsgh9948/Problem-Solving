dx = [-1,0,1,0]
dy = [0,1,0,-1]

cctv_range = [
    [],
    [0],
    [0,2],
    [0,1],
    [0,1,2],
    [0,1,2,3]
]
n,m = map(int, input().strip().split())

cctvs = []
board = []
safe_zone_cnt = 0
ans = 1000000000
for i in range(n):
    board.append(input().strip().split())
    for j in range(m):
        if '1' <= board[i][j] and board[i][j] <= '5':
            cctvs.append((i,j,int(board[i][j])))
        elif board[i][j] == '0':
            safe_zone_cnt += 1

def select_cctv_dir(idx,cctv_dir):
    if idx == len(cctvs):
        simul(cctv_dir)
        return
    x,y,cctv_type = cctvs[idx]
    if cctv_type == 5:
        cctv_dir[idx] = 0
        select_cctv_dir(idx+1, cctv_dir)
    else:
        for d in range(4):
            cctv_dir[idx] = d
            select_cctv_dir(idx+1, cctv_dir)

def simul(cctv_dir):
    temp_board = []

    copy_board(board,temp_board)

    cctv_range_cnt = 0
    for i in range(len(cctvs)):
        x,y,cctv_type = cctvs[i]
        d = cctv_dir[i]
        for nd in cctv_range[cctv_type]:
            cctv_range_cnt += insert_cctv(x,y,(d+nd)%4,temp_board)

    global ans
    ans = min(ans, safe_zone_cnt-cctv_range_cnt)

def copy_board(src,dest):
    for i in range(n):
        row = []
        for j in range(m):
            row.append(src[i][j])
        dest.append(row)

def insert_cctv(x,y,d,temp_board):
    cnt = 0
    while True:
        if temp_board[x][y] == '0':
            cnt += 1
        temp_board[x][y] = '#'

        nx = x + dx[d]
        ny = y + dy[d]

        if not point_validator(nx,ny,temp_board):
            break
        x,y = nx,ny
    return cnt

def point_validator(x,y,temp_board):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif temp_board[x][y] == '6':
        return False
    return True

select_cctv_dir(0,[0]*len(cctvs))

print(ans)