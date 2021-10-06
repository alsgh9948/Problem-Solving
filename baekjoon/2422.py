from sys import stdin
from itertools import combinations

n,m = map(int, stdin.readline().strip().split())

num = [i for i in range(1,n+1)]
no_mix = [[False]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,stdin.readline().strip().split())
    no_mix[a][b] = True
    no_mix[b][a] = True

def simul():
    cnt = 0
    for selected in combinations(num,3):
        if check_mix(selected):
            cnt += 1

    return cnt

def check_mix(selected):
    for i in range(3):
        a = selected[i]
        for j in range(i+1,3):
            b = selected[j]
            if no_mix[a][b]:
                return False
    return True

print(simul())