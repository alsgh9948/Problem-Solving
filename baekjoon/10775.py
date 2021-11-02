from sys import stdin

input = stdin.readline
g = int(input())
p = int(input())
gate = [i for i in range(g+1)]

def solv():
    global gate
    answer = 0
    for _ in range(p):
        gi = int(input())
        rst = find(gi)
        if rst == 0:
            break
        union(rst-1,gi)
        answer += 1
    print(answer)
def find(target):
    if gate[target] == target:
        return target
    else:
        gate[target] = find(gate[target])
        return gate[target]

def union(a,b):
    global gate
    a = find(a)
    b = find(b)

    if a != b:
        if a > b:
            gate[a] = b
        else:
            gate[b] = a
solv()