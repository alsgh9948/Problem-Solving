from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input())

parent = [[i,1] for i in range(1000001)]
def solv():
    for _ in range(n):
        command = input().strip().split()
        if command[0] == 'I':
            a,b = map(int, command[1:])
            union(a,b)
        else:
            target = int(command[1])
            p = find(target)
            print('%d\n'%(parent[p][1]))
def find(target):
    global parent
    if parent[target][0] == target:
        return parent[target][0]
    else:
        parent[target][0] = find(parent[target][0])
        return parent[target][0]

def union(a,b):
    global parent
    a = find(a)
    b = find(b)

    if a != b:
        if a > b:
            parent[a][0] = parent[b][0]
            parent[b][1] += parent[a][1]
        else:
            parent[b][0] = parent[a][0]
            parent[a][1] += parent[b][1]
solv()