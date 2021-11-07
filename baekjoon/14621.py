from sys import stdin

input = stdin.readline

n,m = map(int, input().split())
typ = ['-']+list(input().strip().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2])

parent = [i for i in range(n+1)]

def solv():
    print(kruskal())

def kruskal():
    edge_count = 0
    cost = 0

    for a,b,c in edges:
        if typ[a] != typ[b]:
            if not is_same_parent(a,b):
                union(a,b)
                edge_count += 1
                cost += c
                if edge_count == n-1:
                    return cost
    return -1

def is_same_parent(a,b):
    return find(a) == find(b)
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