from sys import stdin,stdout
from collections import deque

input = stdin.readline
print = stdout.write
n,t,w = map(int, input().split())
wait_q = deque()

for _ in range(n):
    sp,st = map(int, input().split())
    wait_q.appendleft((sp,st,0))

m = int(input())
nxt_cust = []

for _ in range(m):
    sp,st,sc = map(int, input().split())
    nxt_cust.append((sp,st,sc))

nxt_cust.sort(key=lambda x:(-x[2]))
def solv():
    global wait_q,nxt_cust

    np,ns,nc = wait_q.pop()
    tmp = t
    for now in range(1,w+1):
        if nxt_cust and nxt_cust[-1][2] == now:
            wait_q.appendleft(nxt_cust.pop())

        print('%d\n'%np)
        tmp -= 1
        ns -= 1
        if tmp == 0 or ns == 0:
            if ns > 0:
                wait_q.appendleft((np, ns, nc))
            tmp = t
            if wait_q:
                np,ns,nc = wait_q.pop()
solv()