from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,p = map(int, input().split())

s = [0]+list(map(int, input().split()))
ans_cnt = [0]*len(s)
board = []
p_list = []

for x in range(n):
    board.append(list(input().strip()))
    for y in range(m):
        if board[x][y].isdigit():
            board[x][y] = int(board[x][y])
            ans_cnt[board[x][y]] += 1
            p_list.append((board[x][y],x,y))
        elif board[x][y] == '.':
            board[x][y] = 0
        else:
            board[x][y] = -1

p_list.sort(key=lambda x :-x[0])
def solv():
    global board
    q = deque(p_list)

    while q:
        extend_q = deque()
        target = q[-1][0]
        while q:
            if target == q[-1][0]:
                num, x, y = q.pop()
                extend_q.appendleft((x,y,0))
            else:
                break
        extends(q,extend_q,target)
    print(*ans_cnt[1:])

def extends(q,extend_q,num):
    while extend_q:
        x,y,cnt = extend_q.pop()
        if cnt == s[num]:
            continue
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                ans_cnt[num] += 1
                board[nx][ny] = num
                q.appendleft((num,nx,ny))
                extend_q.appendleft((nx, ny, cnt + 1))
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] != 0:
        return False
    return True
solv()