from sys import stdin
from itertools import combinations

n,m = map(int, stdin.readline().strip().split())

home = []
store = []
board = []

for i in range(n):
    board.append(stdin.readline().strip().split())
    for j in range(n):
        if board[i][j] == '1':
            home.append([i,j,0])
        elif board[i][j] == '2':
            store.append((i,j))

def solv():
    ans = 1000000000
    for comb in combinations(store,m):
        for home_idx in range(len(home)):
            chicken_length = 1000000000
            for store_idx in range(m):
                chicken_length = min(chicken_length, calc_chicken_length(home_idx,store_idx,comb))
            home[home_idx][2] = chicken_length

        total_chicken_length = 0
        for x,y,chicken_length in home:
            total_chicken_length += chicken_length
        ans = min(total_chicken_length,ans)
    print(ans)

def calc_chicken_length(home_idx, store_idx,comb):
    hx,hy,temp = home[home_idx]
    sx,sy = comb[store_idx]
    return abs(hx-sx) + abs(hy-sy)

solv()