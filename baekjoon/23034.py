from sys import stdin
from collections import deque

input = stdin.readline

n,m = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
max_cost_board = [[-1]*(n+1) for _ in range(n+1)]

edges = []
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))

edges.sort(key=lambda x:x[2])

parent = [i for i in range(n+1)]
def solv():
    q = int(input())
    total_cost = kruskal()
    set_max_cost_board()

    for _ in range(q):
        a,b = map(int, input().split())
        print(total_cost-max_cost_board[a][b])
def set_max_cost_board():
    for start in range(1,n+1):
        bfs(start)

def bfs(start):
    global max_cost_board
    max_cost_board[start][start] = 0

    q = deque([(start,0)])

    while q:
        now, max_cost = q.pop()

        for nxt, cost in adj_list[now]:
            if max_cost_board[start][nxt] == -1:
                tmp_max_cost = max(max_cost,cost)
                max_cost_board[start][nxt] = tmp_max_cost
                q.appendleft((nxt,tmp_max_cost))
def kruskal():
    global adj_list
    edge_count = 0
    cost = 0
    for a,b,c in edges:
        if not is_same_parent(a,b):
            union(a,b)
            edge_count += 1
            cost += c
            adj_list[a].append((b,c))
            adj_list[b].append((a,c))
            if edge_count == n-1:
                return cost
def find(target):
    global parent
    if parent[target] == target:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a,b):
    global parent
    a = find(a)
    b = find(b)

    if a != b:
        parent[a] = b

def is_same_parent(a,b):
    return find(a) == find(b)

solv()