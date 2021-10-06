from sys import stdin
from collections import deque

input = stdin.readline
n,k = map(int, input().split())

points = list(map(int, input().split()))

home_dict = {}

q = deque()
answer = 0
for p in points:
    home_dict[p] = 0
    q.appendleft((p,0))

def solv():
    global answer
    h_cnt = 0
    while q:
        now, cnt = q.pop()

        if now-1 not in home_dict:
            q.appendleft((now-1, cnt+1))
            home_dict[now-1] = cnt+1
            answer += cnt+1
            h_cnt += 1
            if h_cnt == k:
                break

        if now+1 not in home_dict:
            q.appendleft((now+1, cnt+1))
            home_dict[now+1] = cnt+1
            answer += cnt+1
            h_cnt += 1
            if h_cnt == k:
                break

    print(answer)
solv()