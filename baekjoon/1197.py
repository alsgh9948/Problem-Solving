from sys import stdin

input = stdin.readline

v,e = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(e)]

edges.sort(key=lambda x:x[2])

parent = [i for i in range(v+1)]
def solv():
    count = 0
    cost = 0
    for a,b,c in edges:
        if not is_same_parent(a,b):
            union(a,b)
            count += 1
            cost += c
            if count == v-1:
                break
    print(cost)
def is_same_parent(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return True
    else:
        return False
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
solv()