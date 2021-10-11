from sys import stdin
from heapq import heappush, heappop

INF = 9876543210

input = stdin.readline
dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,-1,1,1]

n,w = map(int, input().split())
m = float(input())

spot = [{}]
for idx in range(n):
    x,y = map(int, input().split())
    spot.append({
        'num' : idx,
        'pos': (x,y),
        'linked' : set()
    })

for _ in range(w):
    a,b = map(int, input().split())
    spot[a]['linked'].add(b)
    spot[b]['linked'].add(a)

def solv():
    pq = [(0,1)]
    dist = [INF]*(n+1)
    dist[1] = 0
    while pq:
        length,now = heappop(pq)
        if now == n:
            print(int(length*1000))
            return
        if dist[now] != length:
            continue
        for nxt in range(1,n+1):
            if now == nxt:
                continue
            if nxt in spot[now]['linked']:
                nxt_lenth = 0
            else:
                nxt_lenth = calc_length(spot[now]['pos'],spot[nxt]['pos'])
                if nxt_lenth > m:
                    continue
            if dist[nxt] > nxt_lenth+length:
                dist[nxt] = nxt_lenth + length
                heappush(pq,(dist[nxt],nxt))
def calc_length(pos1,pos2):
    return (abs(pos1[0]-pos2[0])**2+abs(pos1[1]-pos2[1])**2)**(1/2)
solv()