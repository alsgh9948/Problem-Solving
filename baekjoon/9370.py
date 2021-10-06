from sys import stdin
from heapq import heappush, heappop

input = stdin.readline
INF = 9876543210

tc = int(input())

def solv():
    n,m,t = map(int, input().split())
    s,g,h = map(int, input().split())

    adj_list = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int, input().split())
        adj_list[a].append((b,c))
        adj_list[b].append((a,c))
    candidate = []
    for _ in range(t):
        candidate.append(int(input()))

    rst = dijkstart1(s,n,g,h,adj_list,candidate)
    print(*rst)
def dijkstart1(s,n,g,h,adj_list,candidate):
    start_status = 0
    if s == g:
        start_status = 1
    elif s == h:
        start_status = 2

    pq = [(0,s,start_status)]
    visited = [[False]*4 for _ in range(n+1)]
    visited[s][start_status] = True
    answer = []

    while pq:
        cost, now, status = heappop(pq)
        tmp = [cost,[]]
        flag = False
        if status == 3:
            if now in candidate:
                tmp[1].append(now)
                answer.append(tmp)
                continue
        for nxt,nxt_cost in adj_list[now]:
            if status == 3:
                if nxt in candidate:
                    tmp[1].append(nxt)
                    flag = True


            nxt_status = status
            if status == 0:
                if nxt == g:
                    nxt_status = 1
                elif nxt == h:
                    nxt_status = 2
            elif status == 1:
                if nxt == h:
                    nxt_status = 3
            elif status == 2:
                if nxt == g:
                    nxt_status = 3
            if not visited[nxt][nxt_status]:
                visited[nxt][nxt_status] = True
                heappush(pq,(cost+nxt_cost,nxt,nxt_status))
        if flag:
            answer.append(tmp)
    answer.sort()
    before = answer[0][0]
    total = answer[0][1]
    for cost, points in answer[1:]:
        if before != cost:
            break
        else:
            before = cost
            total += points
    return sorted(list(set(total)))
for _ in range(tc):
    solv()