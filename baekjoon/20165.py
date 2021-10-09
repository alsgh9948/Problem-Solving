from sys import stdin
from collections import deque

input = stdin.readline
dir = {
    'E':[0,1],
    'W':[0,-1],
    'N':[-1,0],
    'S':[1,0]
}

n,m,r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
orders = []
status_board = [['S'] * m for _ in range(n)]
for _ in range(r):
    order = []
    x,y,d = input().split()
    order.append((int(x)-1,int(y)-1,d))

    x,y = map(int, input().split())
    order.append((x-1,y-1))
    orders.append(order)
def solv():
    score = 0
    for order in orders:
        ax,ay,d = order[0]
        if status_board[ax][ay] == 'S':
            score += attack(ax,ay,d)

        dx,dy = order[1]
        if status_board[dx][dy] == 'F':
            defense(dx,dy)

    print(score)
    for row in status_board:
        print(*row)
def attack(sx,sy,d):
    global status_board
    q = deque([(sx,sy)])
    status_board[sx][sy] = 'F'
    score = 0
    while q:
        x,y = q.pop()
        cnt = board[x][y]
        score += 1
        for _ in range(cnt-1):
            x += dir[d][0]
            y += dir[d][1]

            if not point_validator(x,y):
                break
            if status_board[x][y] == 'S':
                status_board[x][y] = 'F'
                q.appendleft((x,y))
    return score
def defense(x,y):
    global status_board
    status_board[x][y] = 'S'

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True
solv()