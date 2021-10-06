from sys import stdin

input = stdin.readline

tc = int(input())
def solv():
    n = int(input())
    points = []
    xcnt = [0] * 100001
    for _ in range(n):
        x,y = map(int, input().split())
        points.append((x,y))
        xcnt[x] += 1

    points.sort()
    idx = 0
    if points[0][0] != 0 or points[0][1] != 0:
        idx = modify_order(points, idx, xcnt)
    else:
        idx = 1
    while idx < n:
        if points[idx-1][0] != points[idx][0] and points[idx-1][1] != points[idx][1]:
            idx = modify_order(points, idx, xcnt)
        else:
            idx += 1
    targets = list(map(int, input().split()))
    for target in targets[1:]:
        print(*points[target-1])

def modify_order(points, idx, xcnt):
    tmp = points[idx:idx + xcnt[points[idx][0]]]
    op = -1
    start = xcnt[points[idx][0]] - 1
    end = -1

    for j in range(start, end, op):
        points[idx] = tmp[j]
        idx += 1
    return idx
for _ in range(tc):
    solv()