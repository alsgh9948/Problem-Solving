from sys import stdin

input = stdin.readline

tc = int(input())

class Node:
    def __init__(self,idx):
        self.idx = idx
        self.parent = None
        self.children = []

def solv():
    n = int(input())
    nodes = [Node(i) for i in range(n+1)]

    for _ in range(n-1):
        a,b = map(int, input().split())
        nodes[a].children.append(nodes[b])
        nodes[b].parent = nodes[a]
    a,b = map(int, input().split())
    a_parents = search_parent(nodes, a)
    b_parents = search_parent(nodes, b)

    for a_idx in a_parents:
        for b_idx in b_parents:
            if a_idx == b_idx:
                print(a_idx)
                return
def search_parent(nodes, start):
    now = nodes[start]
    parents = [now.idx]
    while now.parent:
        parents.append(now.parent.idx)
        now = now.parent
    return parents
for _ in range(tc):
    solv()