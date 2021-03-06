from sys import stdin

input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))
num_idx = 0
tree = [[] for _ in range(n)]
def solv():
    inorder(0)
    for row in tree:
        print(*row)
def inorder(depth):
    global tree,num_idx
    if depth == n:
        return

    inorder(depth+1)
    tree[depth].append(nums[num_idx])
    num_idx += 1
    inorder(depth+1)

solv()