from sys import stdin, setrecursionlimit
setrecursionlimit(100000)

input = stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n):
    idx,l,r = map(int, input().split())
    tree[idx] = [l,r]

path = []
def solv():
    similar_inorder_travel(1)
    cnt = search_last_node(path)
    print(len(path)-cnt-1)
def search_last_node(path):
    cnt = 0
    for idx in range(len(path)-1,-1,-1):
        now = path[idx]
        if tree[now][0] == -1 or tree[now][1] == -1:
            return cnt
        cnt += 1
def similar_inorder_travel(now):
    global path
    path.append(now)
    if tree[now][0] != -1:
        similar_inorder_travel(tree[now][0])
        path.append(now)

    if tree[now][1] != -1:
        similar_inorder_travel(tree[now][1])
        path.append(now)

solv()