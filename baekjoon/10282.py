from sys import stdin
from heapq import heappush, heappop
from collections import deque

input = stdin.readline
INF = 9876543210

tc = int(input())

def solv():
    n,d,c = map(int, input().split())
    adj_list = set_adj_list(n,d)

    print(*dijkstra(adj_list,n,c))

def dijkstra(adj_list, n, c):
    pq = [(0,c)]
    time_table = [INF]*(n+1)
    time_table[c] = 0

    while pq:
        t,now = heappop(pq)
        while adj_list[now]:
            nxt,cost = adj_list[now].pop()
            time_table[nxt] = min(time_table[nxt],t+cost)
            heappush(pq, (t + cost, nxt))

    total_cnt,total_time = 0,0
    for t in time_table:
        if t != INF:
            total_cnt += 1
            total_time = max(total_time,t)
    return total_cnt, total_time
def set_adj_list(n,d):
    adj_list = [deque() for _ in range(n+1)]

    for _ in range(d):
        a,b,c = map(int, input().split())
        adj_list[b].appendleft((a,c))

    return adj_list
for _ in range(tc):
    solv()