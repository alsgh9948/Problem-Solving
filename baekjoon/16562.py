from sys import stdin

input = stdin.readline

n,m,k = map(int, input().split())
friend_price = list(map(int, input().split()))

parent = [i for i in range(n)]

def solv():
    init()
    if m == 0:
        total = sum(friend_price)
        if k < total:
            print('Oh no')
        else:
            print(total)
    else:
        starts = set(parent)
        total = 0
        visited = [False]*n
        for idx in starts:
            idx = find(idx)
            if not visited[idx]:
                visited[idx] = True
                total += friend_price[idx]
                if k < total:
                    print('Oh no')
                    return
        print(total)

def init():
    for _ in range(m):
        a,b = map(int, input().split())
        union(a-1,b-1)

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
        if friend_price[a] > friend_price[b]:
            parent[a] = b
        else:
            parent[b] = a

solv()