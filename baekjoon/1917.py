from sys import stdin

input = stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

class Dice:
    def __init__(self):
        self.u = False
        self.d = False
        self.l = False
        self.r = False
        self.f = False
        self.b = False

    def move(self,d):
        if d == 0:
            self.__up()
        elif d == 1:
            self.__right()
        elif d == 2:
            self.__down()
        else:
            self.__left()
    def __left(self):
        self.l,self.d,self.r,self.u = self.u,self.l,self.d,self.r
    def __right(self):
        self.r,self.u,self.l,self.d = self.u,self.l,self.d,self.r
    def __up(self):
        self.f,self.u,self.b,self.d = self.u,self.b,self.d,self.f
    def __down(self):
        self.b,self.u,self.f,self.d = self.u,self.f,self.d,self.b
    def is_possible(self):
        if not self.u or not self.d or not self.l or not self.r or not self.f or not self.b:
            return 'no'
        else:
            return 'yes'

boards = [[list(map(int, input().split())) for _ in range(6)] for _ in range(3)]


def solv(board):
    visited = [[False]*6 for _ in range(6)]
    for sx in range(6):
        for sy in range(6):
            if board[sx][sy] == 1:
                dice = Dice()
                dice.d = True
                visited[sx][sy] = True
                is_possible(sx,sy,visited,board,dice)
                print(dice.is_possible())
                return
def is_possible(x,y,visited,board,dice):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if point_validator(nx,ny,visited,board):
            visited[nx][ny] = True
            dice.move(d)
            dice.d = True
            is_possible(nx,ny,visited,board,dice)
            dice.move((d+2)%4)

def point_validator(x,y,visited,board):
    if x < 0 or y < 0 or x >= 6 or y >= 6:
        return False
    elif board[x][y] == 0:
        return False
    elif visited[x][y]:
        return False
    return True

for board in boards:
    solv(board)