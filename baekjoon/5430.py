from sys import stdin
from collections import deque

input = stdin.readline

tc = int(input())

def solv():
    ps = input().strip()
    n = int(input())
    arr = input().strip('[]\n').split(',')
    print(simul(arr,ps))

def simul(arr,ps):
    dq = deque(arr)
    dir = 0

    for p in ps:
        if p == 'R':
            dir = (dir + 1) % 2
        else:
            if not dq or not dq[-1]:
                return 'error'
            if dir == 0:
                dq.popleft()
            else:
                dq.pop()

    ans = []
    while dq:
        if dir == 0:
            ans.append(dq.popleft())
        else:
            ans.append(dq.pop())
    ans = ','.join(ans)
    return f'[{ans}]'
for _ in range(tc):
    solv()
