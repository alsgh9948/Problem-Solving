from sys import stdin
from itertools import combinations

INF = 9876543210
input = stdin.readline

n,m = map(int, input().split())
dist = [[INF]*n for _ in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    dist[a-1][b-1]=dist[b-1][a-1]=1

def solv():
    set_board()
    answer_a=answer_b=0
    answer_total = INF
    for a,b in combinations(range(n),2):
        total = 0
        for idx in range(n):
            if idx in (a,b):
                continue
            total += min(dist[a][idx],dist[b][idx])*2
        if total < answer_total:
            answer_total = total
            answer_a,answer_b=a,b
    print(answer_a+1,answer_b+1,answer_total)
def set_board():
    for k in range(n):
        for i in range(n):
            if k == i:
                continue
            for j in range(n):
                if i == j:
                    continue
                elif dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

solv()