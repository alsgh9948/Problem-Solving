from sys import stdin

input = stdin.readline
calc_dist = lambda p1,p2:(abs(p1[0]-p2[0])**2+abs(p1[1]-p2[1])**2)**(1/2)
n = int(input())
points = []
for _ in range(n):
    points.append(list(map(float, input().split())))

parents = [i for i in range(n)]
edges = []

def solv():
    set_edges()
    print("%.2f"%kruskal())

def kruskal():
    edge_count = 0
    cost = 0

    for a,b,c in edges:
        if not is_same_parent(a,b):
            union(a,b)
            cost += c

            edge_count += 1
            if edge_count == n-1:
                return cost

def find(target):
    if parents[target] == target:
        return target

    parents[target] = find(parents[target])
    return parents[target]

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        parents[a] = b

def is_same_parent(a,b):
    return find(a) == find(b)

def set_edges():
    global edges

    for i in range(n-1):
        for j in range(i+1,n):
            edges.append((i,j,calc_dist(points[i],points[j])))

    edges.sort(key=lambda x:x[2])

solv()