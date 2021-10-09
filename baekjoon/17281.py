from sys import stdin
from itertools import permutations

n = int(stdin.readline())

results = [list(map(int, stdin.readline().split())) for _ in range(n)]

def solv():
    ans = 0
    for order in permutations(range(1,9),8):
        ans = max(ans, simul(list(order)))

    return ans

def simul(order):
    order = order[:3] + [0] + order[3:]
    now = 0
    score = 0
    for result in results:
        out = 0
        base = [0,0,0]
        while out < 3:
            rst = result[order[now]]
            now = (now+1)%9

            if rst == 0:
                out += 1
            elif rst == 1:
                score += base[2]
                base[2] = base[1]
                base[1] = base[0]
                base[0] = 1
            elif rst == 2:
                score += (base[2]+base[1])
                base[2] = base[0]
                base[1] = 1
                base[0] = 0
            elif rst == 3:
                score += (base[2]+base[1]+base[0])
                base[2] = 1
                base[1] = 0
                base[0] = 0
            elif rst == 4:
                score += (base[2]+base[1]+base[0]+1)
                base[2] = 0
                base[1] = 0
                base[0] = 0
    return score

print(solv())