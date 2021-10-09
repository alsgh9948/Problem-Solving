dx = [ 1,1,-1,-1]
dy = [-1,1, 1,-1]
n = int(input())
popular = [list(map(int, input().split())) for _ in range(n)]
total = 0
for row in popular:
    total += sum(row)
def solv():
    global total
    ans = 987654321
    for x in range(n-2):
        for y in range(n-1):
            for d1 in range(1,n-1):
                if x + d1 >= n or y - d1 < 0:
                    break
                for d2 in range(1,n-1):
                    if x + d1 + d2 >= n or y - d1 + d2 >= n:
                        break
                    board = [[0]*n for _ in range(n)]
                    if insert_adge(x,y,d1,d2,board):
                        cnt = calc_cnt(x,y,d1,d2,board)

                        cnt.append(total-sum(cnt))
                        cnt.sort()
                        ans = min(ans,cnt[-1]-cnt[0])
                    else:
                        break

    return ans
def insert_adge(x,y,d1,d2,board):
    cnt = 0
    nx,ny = x,y
    d = 0
    board[nx][ny] = 5
    nx += dx[d]
    ny += dy[d]
    while True:
        board[nx][ny] = 5
        nx += dx[d]
        ny += dy[d]
        cnt += 1

        if d in [0,2] and cnt == d1:
            nx -= dx[d]
            ny -= dy[d]

            d+= 1

            if d == 4:
                break

            nx += dx[d]
            ny += dy[d]
            cnt = 0

        elif d in [1, 3] and cnt == d2:
            nx -= dx[d]
            ny -= dy[d]

            d += 1

            if d == 4:
                break

            nx += dx[d]
            ny += dy[d]
            cnt = 0

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            return False
    return True
def calc_cnt(x,y,d1,d2,board):
    cnt = [0,0,0,0]
    for i in range(x+d1):
        for j in range(y+1):
            if board[i][j] == 5:
                break
            board[i][j] = 1
            cnt[0] += popular[i][j]

    for i in range(x+d2+1):
        for j in range(n-1,y,-1):
            if board[i][j] == 5:
                break
            board[i][j] = 2
            cnt[1] += popular[i][j]

    for i in range(x+d1,n):
        for j in range(y-d1+d2):
            if board[i][j] == 5:
                break
            board[i][j] = 3
            cnt[2] += popular[i][j]

    for i in range(x+d2+1,n):
        for j in range(n-1,y-d1+d2-1,-1):
            if board[i][j] == 5:
                break
            board[i][j] = 4
            cnt[3] += popular[i][j]

    return cnt

def copy_board(src,dest):
    for i in range(n):
        row = []
        for j in range(n):
            row.append(src[i][j])
        dest.append(row)
    return dest

print(solv())