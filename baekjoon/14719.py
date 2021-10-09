from sys import stdin

h,w = map(int, input().split())
height = list(map(int, input().split()))

board = [[False]*w for _ in range(h)]

def set_board():
    global board
    y = 0
    for hh in height:
        x = h-1
        for _ in range(hh):
            board[x][y] = True
            x -= 1
        y += 1
def solv():
    set_board()

    answer = 0
    for x in range(h-1,-1,-1):
        flag = False
        cnt = 0
        for y in range(w):
            if board[x][y]:
                if flag:
                    answer += cnt
                    cnt = 0
                else:
                    flag = True
                    cnt = 0
            else:
                cnt += 1
    print(answer)

solv()