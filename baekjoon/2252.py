from sys import stdin
from collections import deque

input = stdin.readline

n,m = map(int, input().split())
in_degree = [0]*(n+1)
adj_list = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    in_degree[b] += 1
    adj_list[a].append(b)

def solv():
    answer = []
    for start in range(1,n+1):
        if in_degree[start] == 0:
            answer.extend(sort(start))
    print(*answer)
    
def sort(start):
    global in_degree
    q = deque([(start)])
    sort_result = []
    while q:
        now = q.pop()
        sort_result.append(now)
        in_degree[now] = -1

        for nxt in adj_list[now]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.appendleft(nxt)
    return sort_result

solv()