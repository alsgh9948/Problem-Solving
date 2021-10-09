from sys import stdin
from collections import deque

input = stdin.readline

gears = []
for _ in range(4):
    gears.append(list(input().strip()))

k = int(input())
order = []
for _ in range(k):
    num,dir = map(int, input().split())
    order.append((num-1,dir))

def solv():
    simul()
    print(calc_answer())

def calc_answer():
    op = 0
    answer = 0
    for gear in gears:
        if gear[0] == '1':
            answer += 2**op
        op += 1
    return answer
def simul():
    for num, dir in order:
        q = deque()
        if is_roate(num,1):
            q.appendleft((num+1,-dir,1))
        if is_roate(num,-1):
            q.appendleft((num-1,-dir,-1))
        rotate_gear(num,dir)
        while q:
            now,r,d = q.pop()
            if now < 0 or now >= 4:
                continue
            if is_roate(now, d):
                q.appendleft((now+d,-r,d))
            rotate_gear(now, r)

def is_roate(num,d):
    nxt = num+d
    if d == 1:
        if nxt >= 4 or gears[num][2] == gears[nxt][6]:
            return False
        else:
            return True
    else:
        if nxt < 0 or gears[num][6] == gears[nxt][2]:
            return False
        else:
            return True

def rotate_gear(num,r):
    global gears
    if r == 1:
        gears[num] = gears[num][-1:]+gears[num][:-1]
    else:
        gears[num] = gears[num][1:]+gears[num][:1]
solv()