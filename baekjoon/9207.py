from sys import stdin

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

tc = int(input())

board = []
target = [[]]
ans = 987654321

def solv():
    global board, target, ans,target_cnt
    for _ in range(tc):
        board = []
        target = [[]]
        ans = 987654321
        for x in range(5):
            board.append(list(input().strip()))
            for y in range(9):
                if board[x][y] == 'o':
                    board[x][y] = len(target)
                    target.append([x,y,True])
                elif board[x][y] == '.':
                    board[x][y] = 0
                else:
                    board[x][y] = -1
        target_cnt = len(target)-1
        dfs(987654321)
        if ans == 987654321:
            print(target_cnt,0)
        else:
            print(ans, target_cnt-ans)
        input()
def dfs(cnt):
    global board, ans

    if cnt != 987654321:
        ans = min(ans,target_cnt-cnt)
    else:
        cnt = 0
    if ans == 1:
        return True
    for now in range(1,target_cnt+1):
        x,y,status = target[now]
        if status:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if point_validator(nx,ny,1):
                    nnx = nx + dx[d]
                    nny = ny + dy[d]

                    if point_validator(nnx,nny,2):
                        target[now] = [nnx,nny,status]
                        board[x][y], board[nnx][nny] = board[nnx][nny], board[x][y]

                        tmp = board[nx][ny]
                        target[tmp][2] = False
                        board[nx][ny] = 0

                        if dfs(cnt+1):
                            return True

                        target[now] = [x,y,status]
                        board[x][y], board[nnx][nny] = board[nnx][nny], board[x][y]

                        target[tmp][2] = True
                        board[nx][ny] = tmp

    return False
def point_validator(x,y,step):
    if x < 0 or y < 0 or x >= 5 or y >= 9:
        return False
    elif step == 1 and board[x][y] < 1:
        return False
    elif step == 2 and board[x][y] != 0:
        return False
    return True

solv()
