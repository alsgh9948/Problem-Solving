from sys import stdin
from collections import deque
input = stdin.readline

n,k = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(k)]
edges.sort(key=lambda x:x[2])
parents = [i for i in range(n)]
adj_list = [[] for _ in range(n)]
def solv():
    total_cost = kruskal()
    max_dist = 0

    for start in range(n):
        if len(adj_list[start]) == 1:
            max_dist = max(max_dist, bfs(start))
    print(total_cost)
    print(max_dist)
def bfs(start):
    visited = [False] * n
    q = deque([(start,0)])
    visited[start] = True
    max_dist = 0
    while q:
        now,dist = q.pop()
        max_dist = dist if max_dist < dist else max_dist
        for nxt, cost in adj_list[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.appendleft((nxt,dist+cost))
    return max_dist
def find(target):
    global parents

    if parents[target] == target:
        return target
    parents[target] = find(parents[target])
    return parents[target]

def union(a, b):
    global parents
    a = find(a)
    b = find(b)

    if a != b:
        parents[a] = b

def is_same_parent(a,b):
    return find(a) == find(b)

def kruskal():
    global adj_list
    edge_count = 0
    cost = 0
    for a,b,c in edges:
        if not is_same_parent(a,b):
            adj_list[a].append((b,c))
            adj_list[b].append((a,c))
            union(a,b)
            edge_count += 1
            cost += c
            if edge_count == n-1:
                return cost
solv()