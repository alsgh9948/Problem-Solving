from sys import stdin

input = stdin.readline

n,l,m = map(int, input().split())

fish = []
fish_num = set()

for _ in range(m):
    x,y = map(int, input().split())
    fish.append((x-1,y-1))
    idx = (x-1)*n+y-1
    fish_num.add(idx)
def solv():
    answer = 0
    for x,y in fish:
        for l1 in range(1,l//2):
            l2 = l//2-l1
            for sx in range(max(0,x-l1),x+1):
                for sy in range(max(0,y-l2),y+1):
                    ex = sx + l1+1
                    ey = sy + l2+1
                    answer = max(answer,count_fish(sx,sy,ex,ey))
    print(answer)

def count_fish(sx,sy,ex,ey):
    cnt = 0
    if ex > n or ey > n:
        return 0
    for x in range(sx, ex):
        for y in range(sy, ey):
            idx = x*n+y
            if idx in fish_num:
                cnt += 1
    return cnt

solv()