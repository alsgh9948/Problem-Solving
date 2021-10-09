from sys import stdin

input = stdin.readline

n = int(input())
board = [0]*1001

max_h = 0
for _ in range(n):
    l,h = map(int, input().split())
    board[l] = h
    max_h = max(max_h,h)
def solv():
    set_board()
    std = board.index(max_h)
    answer = calc_size(0,std,1) + calc_size(len(board)-1,std,-1) + max_h

    print(answer)
def calc_size(start, end, op):
    total = 0
    cnt = 0
    target = board[start]
    for idx in range(start,end,op):
        h = board[idx]
        if target >= h:
            cnt += 1
        elif target < h:
            total += cnt*target
            target = h
            cnt = 1
    total += cnt * target
    return total
def set_board():
    global board

    for idx in range(1, 1001):
        if board[idx] != 0:
            board = board[idx:]
            break

    for idx in range(len(board)-1, -1, -1):
        if board[idx] != 0:
            board = board[:idx+1]
            break

if n == 1:
    print(max_h)
else:
    solv()