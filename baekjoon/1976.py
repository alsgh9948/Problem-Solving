from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n)]
def solv():
    for x in range(n):
        row = list(map(int, input().split()))
        for y in range(n):
            if row[y] == 1:
                union(x,y)

    targets = list(map(int, input().split()))
    parent = find(targets[0]-1)
    for target in targets[1:]:
        if parent != find(target-1):
            print('NO')
            return
    print('YES')
def find(target):
    if parent[target] == target:
        return target
    else:
        parent[target] = find(parent[target])
        return parent[target]
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        if a > b:
            parent[b] = a
        else:
            parent[a] = b
solv()