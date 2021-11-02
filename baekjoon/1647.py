from sys import stdin

input = stdin.readline

n,m = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2])
parent = [i for i in range(n+1)]

def solv():
    print(kruskal())
def kruskal():
    edge_count = 0
    cost = 0
    for a,b,c in edges:
        if not is_same_parent(a,b):
            union(a,b)
            cost += c
            edge_count += 1
            if edge_count == n-2:
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
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

def is_same_parent(a,b):
    return find(a) == find(b)
solv()