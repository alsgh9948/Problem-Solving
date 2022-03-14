from sys import stdin
from itertools import combinations

input = stdin.readline

n,m = map(int, input().split())

board = []
chickens = []
homes = []
for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(n):
        if board[x][y] == 1:
            homes.append((x,y))
        elif board[x][y] == 2:
            chickens.append((x,y))

chicken_dist_map = [[0]*len(chickens) for _ in range(len(homes))]
def solv():
    set_chicken_dist()

    answer = 9876543210
    for comb in combinations(range(len(chickens)),m):
        tmp = 0
        for h in range(len(homes)):
            dist = 9876543210
            for c in comb:
                dist = min(dist, chicken_dist_map[h][c])
            tmp += dist
        answer = min(answer, tmp)

    print(answer)

def set_chicken_dist():
    global chicken_dist_map

    for i in range(len(homes)):
        for j in range(len(chickens)):
            dist = abs(homes[i][0] - chickens[j][0]) + abs(homes[i][1] - chickens[j][1])
            chicken_dist_map[i][j] = dist

solv()