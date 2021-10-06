from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

n = int(input())
station_count = list(map(int, input().split()))

m = int(input())
transfer_station = [[[] for _ in range(max(station_count))] for _ in range(n+1)]
transfer_distance = [[[0,0] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b,c,d = map(int, input().split())
    transfer_station[a][b] = c
    transfer_station[c][d] = a
    transfer_distance[a][c] = [1,d]

for k in range(1,n+1):
    for i in range(1,n+1):
        if k == i:
            continue
        for j in range(1,n+1):
            if i == j:
                continue
            elif transfer_distance[i][j][0] > transfer_distance[i][k][0] + transfer_distance[k][j][0]:
                transfer_distance[i][j] = [transfer_distance[i][k][0] + transfer_distance[k][j][0],transfer_distance[i][j][1]]
def solv():
    k = int(input())
    for _ in range(k):
        t,u1,u2,v1,v2 = map(int, input().split())
        if u1 == v1:
            print(abs(u1-v1))
        else:
            print(abs(u2-transfer_distance[u1][v1][1]) + t*transfer_distance[u1][v1][0] + abs(v2-transfer_distance[v1][u1][1])+t)
solv()