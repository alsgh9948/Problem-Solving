from sys import stdin
from heapq import heappush , heappop

input = stdin.readline

n = int(input())

def solv():
    l_pq = []
    r_pq = []
    mid = 0
    for i in range(n):
        num = int(input())
        if i == 0:
            mid = num
        elif i == 1:
            if mid < num:
                heappush(r_pq,num)
            else:
                heappush(l_pq,-mid)
                mid = num
        else:
            if len(l_pq) < len(r_pq):
                if mid > num:
                    heappush(l_pq,-mid)
                    mid = num
                else:
                    mid = -heappop(l_pq)
                    heappush(l_pq, num)
            elif len(l_pq) > len(r_pq):
                if mid > num:
                    heappush(r_pq,mid)
                    mid = num
                else:
                    mid = heappop(r_pq)
                    heappush(r_pq,num)
            else:
                if mid < num:
                    heappush(r_pq, mid)
                else:
                    mid = -heappop(l_pq)
                    heappush(l_pq, -mid)
        print(mid)

solv()