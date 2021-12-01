from sys import stdin

input = stdin.readline

n = int(input())
costs = [int(input()) for _ in range(n)]

edges = []
for x in range(n):
    row = list(map(int, input().split()))
    for y in range(n):
        if x == y:
            edges.append((n,y,costs[y]))
        edges.append((x,y,row[y]))

edges.sort(key=lambda x:x[2])
parent = [i for i in range(n+1)]

def solv():
    print(kruskal())
def kruskal():
    edges_count = 0
    cost = 0
    for a,b,c in edges:
        if not is_same_parent(a,b):
            union(a,b)
            edges_count += 1
            cost += c
            if edges_count == n:
                return cost
    return cost
def find(target):
    global parent
    if parent[target] == target:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a,b):
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