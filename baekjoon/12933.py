from sys import stdin
from collections import deque
input = stdin.readline

quack = deque(list(input().strip()))

def solv():
    global quack
    cnt = 0
    order = 'quack'
    while quack:
        q_len = len(quack)
        order_idx = 0
        flag = False
        for _ in range(q_len):
            now = quack.popleft()
            if now == order[order_idx]:
                order_idx = (order_idx+1)%5
                flag = True
            else:
                quack.append(now)
        if order_idx != 0 or not flag:
            return -1
        else:
            cnt += 1
    return cnt
print(solv())