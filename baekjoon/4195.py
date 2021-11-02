from sys import stdin

input = stdin.readline

tc = int(input())

def solv():
    global parent
    f = int(input())
    parent = [[i,1] for i in range(f*2)]
    friend_index = {}

    for _ in range(f):
        a,b = input().split()
        if a not in friend_index:
            friend_index[a] = len(friend_index)

        if b not in friend_index:
            friend_index[b] = len(friend_index)

        a,b = friend_index[a],friend_index[b]
        union(a,b)
        print(parent[find(a)][1])

def find(target):
    global parent
    if parent[target][0] == target:
        return target
    else:
        parent[target][0] = find(parent[target][0])
        return parent[target][0]

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        if parent[a][1] > parent[b][1]:
            parent[a][0] = b
            parent[b][1] += parent[a][1]
        else:
            parent[b][0] = a
            parent[a][1] += parent[b][1]

for _ in range(tc):
    solv()