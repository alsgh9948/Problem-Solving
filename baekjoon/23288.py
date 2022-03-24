from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

class Dice:
    __U = 0
    __R = 1
    __D = 2
    __L = 3
    def __init__(self):
        self.front = 2
        self.back = 5
        self.up = 1
        self.down = 6
        self.left = 4
        self.right = 3

    def move(self,x,y,d):
        for _ in range(2):
            nx = x + dx[d]
            ny = y + dy[d]

            if boundary_validator(nx, ny):
                x, y = nx, ny
                break
            else:
                d = (d + 2) % 4

        if d == self.__U:
            self.__rotate_up()
        elif d == self.__R:
            self.__rotate_right()
        elif d == self.__D:
            self.__rotate_down()
        elif d == self.__L:
            self.__rotate_left()
        return x,y,d

    def __rotate_up(self):
        self.up,self.front,self.down,self.back = self.back,self.up,self.front,self.down
    def __rotate_left(self):
        self.left,self.down,self.right,self.up = self.up,self.left,self.down,self.right
    def __rotate_right(self):
        self.right,self.down,self.left,self.up = self.up,self.right,self.down,self.left
    def __rotate_down(self):
        self.down,self.back,self.up,self.front = self.back,self.up,self.front,self.down

n,m,k = map(int, input().split())
board = [list(map(int, input().split())) for _ in  range(n)]

dice = Dice()
count_board = [[0]*m for _ in range(n)]
def solv():
    x,y,d = 0,0,1
    answer = 0
    for _ in range(k):
        x,y,d = dice.move(x,y,d)
        if count_board[x][y] == 0:
            bfs(x,y)

        answer += count_board[x][y]*board[x][y]
        d = change_dir(x,y,d)
    print(answer)

def change_dir(x,y,d):
    if dice.down > board[x][y]:
        d = (d+1)%4
    elif dice.down < board[x][y]:
        d = (d-1)%4
    return d
def bfs(sx,sy):
    global count_board
    visited = [[False]*m for _ in range(n)]

    q = deque([(sx,sy)])
    count = 0

    visited[sx][sy] = True
    points = [(sx,sy)]
    target = board[sx][sy]
    while q:
        x,y = q.pop()
        count += 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,target,visited):
                visited[nx][ny] = True
                points.append((nx,ny))
                q.appendleft((nx,ny))

    for x,y in points:
        count_board[x][y] = count

def point_validator(x,y,target,visited):
    if not boundary_validator(x,y):
        return False
    elif board[x][y] != target:
        return False
    elif visited[x][y]:
        return False
    return True

def boundary_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

solv()