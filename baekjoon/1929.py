import sys, math

prim_check = [True for _ in range(1000001)]
prim_check[1] = False

n,m = map(int,sys.stdin.readline().split())

for i in range(2,int(math.sqrt(m))+1):
    if not prim_check[i]:
        continue
    for j in range(i*i,m+1, i):
        prim_check[j] = False

for i in range(n,m+1):
    if prim_check[i]:
        print(i)
