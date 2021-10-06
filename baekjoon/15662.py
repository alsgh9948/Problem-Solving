from sys import stdin
from collections import deque
t = int(stdin.readline().strip())

gears = [list(stdin.readline().strip()) for _ in range(t)]

k = int(stdin.readline().strip())

dir_list = [tuple(map(int, stdin.readline().strip().split())) for _ in range(k)]

def simul():
    for gear_num, r in dir_list:
        q = deque()

        gear_num -= 1
        if is_rotate_gear(gear_num, 1):
            q.appendleft((1,-r,gear_num+1))

        if is_rotate_gear(gear_num, -1):
            q.appendleft((-1,-r,gear_num-1))

        rotate_gear(gear_num, r)

        while q:
            d, r, now = q.pop()

            if is_rotate_gear(now,d):
                q.appendleft((d,-r,now+d))

            rotate_gear(now,r)

    cnt = 0

    for gear in gears:
        if gear[0] == '1':
            cnt+=1

    return cnt

def rotate_gear(gear_num, r):
    global gears
    gear = gears[gear_num]
    if r == 1:
        gear = gear[-1:] + gear[:-1]
    else:
        gear = gear[1:] + gear[:1]
    gears[gear_num] = gear

def is_rotate_gear(now,dir):
    nxt = now+dir
    if nxt < 0 or nxt >= t:
        return False

    if dir == 1:
        if gears[now][2] != gears[nxt][6]:
            return True
        else:
            return False
    else:
        if gears[now][6] != gears[nxt][2]:
            return True
        else:
            return False
print(simul())