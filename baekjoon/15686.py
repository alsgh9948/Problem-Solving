from sys import stdin
from itertools import combinations

input = stdin.readline

n,m = map(int, input().split())
board = []
home = []
chicken = []
for x in range(n):
    board.append(input().strip().split())
    for y in range(n):
        if board[x][y] == '1':
            home.append((x,y))
        elif board[x][y] == '2':
            chicken.append((x,y))

def solv():
    answer = 9876543210

    for comb in combinations(chicken,m):
        total = 0
        for sx,sy in home:
            length = 9876543210
            for ex,ey in comb:
                length = min(length,abs(sx-ex)+abs(sy-ey))
            total += length
        answer = min(answer,total)

    print(answer)
solv()