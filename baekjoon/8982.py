from sys import stdin

input = stdin.readline

n = int(input())
points = []
size = 0
input()
for _ in range(n//2-1):
    sy,sx = map(int, input().split())
    ey,ex = map(int, input().split())
    points.append((sx,sy,ey-sy))
    size += sx*(ey-sy)

input()
m = int(input())
holes = []
for _ in range(m):
    sy,sx,ey,ex = map(int, input().split())
    holes.append([sx,sy,ex,ey])

holes.sort(key=lambda x:x[1])
def solv():
    hole_idx = 1
    answer = 0
    max_h = holes[0][0]
    before_max_h = holes[0][0]
    for x,y,length in points:
        if hole_check(hole_idx,x,y,length):
            max_h = x

        if x >= max_h:
            answer += max_h*length
        elif x >= before_max_h:
            answer += before_max_h*length
        else:
            answer += x*length
            before_max_h = x

    print(size-answer)

def hole_check(hole_idx,x,y,length):
    if hole_idx >= m:
        return False
    elif holes[hole_idx][0] == x and y <= holes[hole_idx][1] <= y+length:
        return True
solv()