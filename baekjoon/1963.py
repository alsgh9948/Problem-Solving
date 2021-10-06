from sys import stdin
from collections import deque

input = stdin.readline

tc = int(input())

prim_num = [True]*10000
visited = [0]*10000
visited_num = 0
def set_prime():
    global prim_num
    for i in range(2,100):
        if prim_num[i]:
            for j in range(i+i,10000,i):
                prim_num[j] = False
def solv():
    a,b = input().strip().split()

    q = deque([(a,0)])
    visited[int(a)] = visited_num

    while q:
        now,cnt = q.pop()
        if now == b:
            print(cnt)
            return

        for idx in range(4):
            for num in range(0,10):
                if idx == 0 and num == 0:
                    continue
                new_num = now[:idx]+str(num)+now[idx+1:]
                int_new_num = int(new_num)
                if prim_num[int_new_num] and visited[int_new_num] != visited_num:
                    visited[int_new_num] = visited_num
                    q.appendleft((new_num,cnt+1))

    print('Impossible')

set_prime()
for _ in range(tc):
    visited_num += 1
    solv()