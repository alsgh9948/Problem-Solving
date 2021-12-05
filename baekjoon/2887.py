from sys import stdin

input = stdin.readline

n = int(input())

points = [list(map(int, input().split()))+[i] for i in range(n)]
edges = []

parent = [i for i in range(n)]
def solv():
    set_edges()
    print(kruskal())

def kruskal():
    edge_count = 0
    cost = 0
    for a,b,c in edges:
        if not is_same_parent(a,b):
            union(a,b)
            edge_count += 1
            cost += c
            if edge_count == n-1:
                return cost
def find(target):
    if parent[target] == target:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[a] = b

def is_same_parent(a,b):
    return find(a) == find(b)

def set_edges():
    global edges

    for i in range(3):
        points.sort(key=lambda x:x[i])
        for idx in range(n-1):
            a = points[idx]
            b = points[idx+1]
            edges.append((a[3],b[3],min(abs(a[0]-b[0]),abs(a[1]-b[1]),abs(a[2]-b[2]))))
    edges.sort(key=lambda x:x[2])
solv()