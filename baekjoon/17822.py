from sys import stdin
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,t = map(int, stdin.readline().split())

board = []

total = 0
num_cnt = 0
for i in range(n):
    board.append(list(map(int, stdin.readline().split())))
    for j in range(m):
        total += board[i][j]
        num_cnt += 1
op_list = []

for _ in range(t):
    x,d,k = list(map(int, stdin.readline().split()))
    op_list.append((x,d,k))

def solv():
    for x,d,k in op_list:
        rotate(x,d,k)
        remove_num()
        if total == 0:
            break
    print(total)
def rotate(x,d,k):
    global board
    for num in range(x-1,n,x):
        new_row = [0]*m
        for idx in range(m):
            if d == 0:
                new_pos = (idx+k%m)%m
            else:
                new_pos = (idx+m-(k%m))%m
            new_row[new_pos] = board[num][idx]
        board[num] = new_row

def remove_num():
    global board, total, num_cnt
    search_flag = False
    for sx in range(n):
        for sy in range(m):
            if board[sx][sy] > 0:
                q = deque()
                q.appendleft((sx,sy))
                target = board[sx][sy]
                flag = False
                while q:
                    x,y = q.pop()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if d == 2 and ny < 0:
                            ny = m-1
                        elif d == 3 and ny >= m:
                            ny = 0
                        if (x == 0 and nx < 0) or (x == n-1 and nx >= n):
                            continue

                        if board[nx][ny] == target:
                            flag = False
                            total -= target
                            num_cnt -= 1
                            board[nx][ny] = 0
                            q.appendleft((nx,ny))
                            search_flag = True
                if flag:
                    total -= target
                    num_cnt -= 1
                    board[sx][sy] = 0
    if not search_flag and total > 0:
        renew_board()
def renew_board():
    global board, total
    avg = total/num_cnt

    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                if board[i][j] > avg:
                    board[i][j] -= 1
                    total -= 1
                elif board[i][j] < avg:
                    board[i][j] += 1
                    total += 1
solv()