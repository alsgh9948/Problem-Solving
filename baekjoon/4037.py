from sys import stdin

input = stdin.readline

tc = int(input())

def solv():
    l,n = map(int, input().split())
    max_ans = 0
    ants = []
    mid_num = l//2
    mid = l
    for _ in range(n):
        ant = int(input())
        ants.append(ant)
        if abs(mid_num-mid) > abs(mid_num-ant):
            mid = ant
        max_ans = max(max_ans, max(l-ant,ant))
    min_ans = min(mid,l-mid)
    print(min_ans,max_ans)
for _ in range(tc):
    solv()