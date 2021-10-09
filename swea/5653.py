from collections import deque

tc = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def solv(t):
    global n,m,k,board,cell_q
    n,m,k = map(int, input().split())
    board = [[[0,0] for _ in range(401)] for _ in range(401)]
    cell_q = deque()

    for x in range(50,50+n):
        row = list(map(int, input().split()))
        for y in range(50,50+m):
            board[x][y][0] = row[y-50]
            if board[x][y][0] != 0:
                cell_q.appendleft((x,y))

    simul()
    answer = 0
    for x in range(401):
        for y in range(401):
            if board[x][y][0] > 0:
              answer += 1
    print('#%d %d'%(t,answer))
def simul():
    global board, cell_q
    new_cell = []
    for t in range(1,k+1):
        cnt_cell = len(cell_q)
        renew_board(new_cell)
        for _ in range(cnt_cell):
            x,y = cell_q.pop()
            if board[x][y][1] < 0:
                board[x][y][1] -= 1
                if board[x][y][1] + board[x][y][0] == -1:
                    board[x][y][0] = -1
                    continue
            else:
                board[x][y][1] += 1
                if board[x][y][1] >= 0 and board[x][y][0] <= board[x][y][1]:
                    spred_cell(x,y,new_cell)
                    board[x][y][1] = -1
            cell_q.appendleft((x,y))
def spred_cell(x,y,new_cell):
    global board,cell_q
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if point_validator(nx,ny):
            new_cell.append((nx,ny,board[x][y][0]))

def renew_board(new_cell):
    global board,cell_q
    while new_cell:
        x,y,hp = new_cell.pop()
        if board[x][y][0] == 0:
            cell_q.appendleft((x, y))
        board[x][y] = [max(hp,board[x][y][0]),0]

def point_validator(x,y):
    if board[x][y][0] != 0:
        return False
    return True
for t in range(1,tc+1):
    solv(t)
