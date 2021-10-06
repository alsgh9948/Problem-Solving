from collections import deque
from itertools import combinations

dx = [0,-1,0]
dy = [-1,0,1]
n,m,d = map(int, input().strip().split())

origin_board = [list(input().strip().split()) for _ in range(n)]
board = []
ans = 0
def solv():
    for archer in combinations([i for i in range(m)],3):
        copy_body()
        simul(archer)

def simul(archer):
    kill_cnt = 0
    for i in range(n-1,-1,-1):
        x = i+1
        kill_enemy = attach_enemy(archer,x)

        for x,y in kill_enemy:
            board[x][y] = '0'
            kill_cnt += 1
    global ans
    ans = max(ans, kill_cnt)

def attach_enemy(archer,sx):
    kill = set()
    for sy in archer:
        q = deque()
        q.appendleft((sx,sy,0))
        flag = False
        while q:
            x,y,length = q.pop()

            if length == d:
                continue
            for dir in range(3):
                nx = x + dx[dir]
                ny = y + dy[dir]

                if not point_validator(nx,ny,sx):
                    continue

                if board[nx][ny] == '1':
                    kill.add((nx,ny))
                    flag = True
                    break
                q.appendleft((nx,ny,length+1))
            if flag:
                break

    return kill
def point_validator(x,y,sx):
    if x < 0 or x >= sx or y < 0 or y >= m:
        return False
    return True

def copy_body():
    global board
    board = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(origin_board[i][j])
        board.append(row)
solv()
print(ans)