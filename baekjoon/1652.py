from sys import stdin

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())

board = [input().strip() for _ in range(n)]

def solv():
    row = check_area()
    rotate_board()
    col = check_area()

    print(row,col)
def check_area():
    count = 0
    for x in range(n):
        tmp = 0
        for y in range(n):
            if board[x][y] == 'X':
                if tmp >= 2:
                    count += 1
                tmp = 0
            else:
                tmp += 1
        if tmp >= 2:
            count += 1
    return count

def rotate_board():
    tmp = []
    for y in range(n):
        row = []
        for x in range(n):
            row.append(board[x][y])
        tmp.append(row)
    for x in range(n):
        board[x] = tmp[x]

solv()