from sys import stdin

input = stdin.readline

n = int(input())
points = []
size = 0
input()
for _ in range(n//2-1):
    sy,sx = map(int, input().split())
    ey,ex = map(int, input().split())
    points.append([sx,sy,ey-sy,0])
    size += sx*(ey-sy)

input()
m = int(input())
holes = []
for _ in range(m):
    sy,sx,ey,ex = map(int, input().split())
    holes.append([sx,sy,ex,ey])

holes.sort(key=lambda x:x[1])

def solv():
    global size
    hole_idx = 0
    for idx in range(n//2-1):
        x, y, length, water = points[idx]
        if hole_idx < m and holes[hole_idx][0] == x and holes[hole_idx][1] == y:
            hole_idx += 1
            renew_water(idx,-1,x,-1)
            renew_water(idx+1, n//2, x,1)

    for idx in range(n//2-1):
        size -= points[idx][3]*points[idx][2]
    print(size)

def renew_water(start,end,h,op):
    global points

    for idx in range(start,end,op):
        if idx >= len(points):
            return
        if points[idx][3] < h:
            if points[idx][0] < h:
                h = points[idx][0]
            points[idx][3] = h
        else:
            break

solv()