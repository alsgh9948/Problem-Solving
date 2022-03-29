from sys import stdin

input = stdin.readline

n,m,k = map(int, input().split())
board = [[0]*m for _ in range(n)]

stickers = []
for _ in range(k):
    r,c = map(int, input().split())
    stickers.append([list(map(int, input().split())) for _ in range(r)])

def solv():
    for sticker in stickers:
        for _ in range(4):
            r, c = len(sticker), len(sticker[0])
            x,y = search_locations(r,c,sticker)
            if x != -1:
                insert_sticker(x,y,r,c,sticker)
                break
            sticker = rotate_sticker(r,c,sticker)
        else:
            continue
    answer = 0
    for row in board:
        answer += row.count(1)
    print(answer)
def search_locations(r,c,sticker):
    ex = n-r+1
    ey = m-c+1
    for x in range(ex):
        for y in range(ey):
            if is_possible(x,y,r,c,sticker):
                return x,y
    return -1,-1

def is_possible(sx,sy,r,c,sticker):
    for x in range(r):
        for y in range(c):
            if sticker[x][y] == 1 and board[sx+x][sy+y] == 1:
                return False
    return True

def rotate_sticker(r,c,sticker):
    new_sticker = []
    for y in range(c):
        row = []
        for x in range(r-1,-1,-1):
            row.append(sticker[x][y])
        new_sticker.append(row)
    return new_sticker
def insert_sticker(sx,sy,r,c,sticker):
    global board
    for x in range(sx,sx+r):
        for y in range(sy,sy+c):
            if sticker[x-sx][y-sy] == 1:
                board[x][y] = 1
solv()
