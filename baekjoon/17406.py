from sys import stdin
from itertools import permutations

dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,m,k = map(int, stdin.readline().split())

input_board = [list(map(int, stdin.readline().split())) for _ in range(n)]

commands = []
for _ in range(k):
    r, c, s = map(int, stdin.readline().split())
    commands.append((r-1,c-1,s))

def solv():
    ans = 987564321
    for command in permutations(commands,k):
        board = copy_board(input_board,[])
        for r,c,s in command:
            rotate(r,c,s,board)
        ans = min(ans,calc_ans(board))
    return ans

def calc_ans(board):
    min_sum = 987654321
    for row in board:
        min_sum = min(min_sum,sum(row))
    return min_sum
def rotate(r,c,s,board):
    for cnt in range(1,s+1):
        sx = r-cnt
        sy = c-cnt
        gx = r+cnt
        gy = c+cnt

        if sx < 0 or sy < 0 or gx >= n or gy >= m:
            return

        d = 0
        temp = board[sx][sy]
        nx,ny = sx,sy
        while True:
            nx += dx[d]
            ny += dy[d]

            if nx < sx or ny < sy or nx > gx or ny > gy:
                nx -= dx[d]
                ny -= dy[d]

                d += 1
                if d == 4:
                    break

                nx += dx[d]
                ny += dy[d]

            board[nx][ny], temp = temp, board[nx][ny]

def copy_board(src,dest):
    for i in range(n):
        row = []
        for j in range(m):
            row.append(src[i][j])
        dest.append(row)
    return dest

print(solv())