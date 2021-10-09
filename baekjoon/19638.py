from sys import stdin
from heapq import heappush, heappop
from math import floor
input = stdin.readline

n,h,t = map(int, input().split())
giant = []
pq = [(-h,True)]
for _ in range(n):
    gh = int(input())
    heappush(pq,(-gh,False))

def solv():
    global pq
    if pq[0][1]:
        print('YES')
        print(0)
    else:
        for cnt in range(1,t+1):
            now_h,typ = heappop(pq)
            if -now_h == 1:
                break
            heappush(pq,(-floor(-now_h/2),typ))
            if pq[0][1]:
                print('YES')
                print(cnt)
                return
        print('NO')
        print(-pq[0][0])

solv()