from sys import stdin

input = stdin.readline

n = int(input())
box = [0]+list(map(int, input().split()))
cnt = [1]*(n+1)
def solv(now):
    global cnt
    if now > n:
        return

    for nxt in range(now+1, n+1):
        if box[now] < box[nxt]:
            if cnt[nxt] < cnt[now]+1:
                cnt[nxt] = cnt[now]+1
                solv(nxt)

for start in range(1,n+1):
    solv(start)
print(max(cnt))