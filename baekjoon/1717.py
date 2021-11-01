from sys import stdin,stdout

input = stdin.readline
print = stdout.write
n,m = map(int, input().split())


parent = [i for i in range(n+1)]

def solv():
    for _ in range(m):
        command, a, b = map(int, input().split())
        if command == 0:
            union(a,b)
        else:
            print('YES\n' if find(a) == find(b) else 'NO\n')

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        if a > b:
            parent[b] = a
        else:
            parent[a] = b
def find(target):
    if parent[target] == target:
        return target
    else:
        parent[target] = find(parent[target])
        return parent[target]
solv()