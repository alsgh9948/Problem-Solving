from sys import stdin
from itertools import permutations

input = stdin.readline

tc = int(input())

def solv():
    global infos,answer
    infos = [list(map(int, input().split())) for _ in range(11)]
    answer = 0
    select_pos(0,[False]*11,0)
    print(answer)

def select_pos(now,select,total):
    global answer
    if now == 11:
        answer = max(answer, total)
        return

    for pos in range(11):
        status = infos[now][pos]
        if status == 0 or select[pos]:
            continue
        select[pos] = True
        select_pos(now+1,select,total+status)
        select[pos] = False

for _ in range(tc):
    solv()