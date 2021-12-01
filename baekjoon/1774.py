from sys import stdin

input = stdin.readline

n,m = map(int, input().split())

locations = [tuple(map(int, input().split())) for _ in range(n)]
edges = []
parent = [i for i in range(n)]

def solv():
    global edges
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a-1,b-1,0))
    set_edges()
    print('%.2f'%kruskal())
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
        for b in range(a+1,n):
            dist = ((locations[a][0]-locations[b][0])**2+(locations[a][1]-locations[b][1])**2)**(1/2)
            edges.append((a,b,dist))

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