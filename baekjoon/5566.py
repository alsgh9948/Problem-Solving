from sys import stdin

input = stdin.readline

n,m = map(int, input().split())

board = []
dice = []

for _ in range(n):
    board.append(int(input()))

for _ in range(m):
    dice.append(int(input()))

def solv():
    now = 0
    for idx in range(m):
        num = dice[idx]
        now += num
        if now >= n-1:
            print(idx+1)
            return
        now += board[now]
        if now >= n-1:
            print(idx+1)
            return

solv()