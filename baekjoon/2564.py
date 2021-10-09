from sys import stdin

input = stdin.readline

m,n = map(int, input().split())

k = int(input())

def trans_position(d,step):
    if d == 1:
        return n+m+n+(m-step)
    elif d == 2:
        return n+step
    elif d == 3:
        return step
    else:
        return n+m+(n-step)

store = []
for _ in range(k):
    d, step = map(int, input().split())
    store.append(trans_position(d, step))

d, step = map(int, input().split())
dong = trans_position(d, step)

def solv():
    answer = 0
    total_dist = (2 * n + 2 * m)
    for p in store:
        dist = max(dong,p)-min(dong,p)
        answer += min(dist, total_dist-dist)
    print(answer)

solv()