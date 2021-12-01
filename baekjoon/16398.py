from sys import stdin

input = stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
edges = []
parent = [i for i in range(n)]

def solv():
    set_edges()
    print(kruskal())
def kruskal():
    edge_count = 0
    cost = 0
    for a,b,c in edges:
        if find(a) != find(b):
            union(a,b)
            edge_count += 1
            cost += c
            if edge_count == n-1:
                return cost
    return 0
def set_edges():
    global edges
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            edges.append((a,b,board[a][b]))
    edges.sort(key=lambda x:x[2])
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
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
solv()