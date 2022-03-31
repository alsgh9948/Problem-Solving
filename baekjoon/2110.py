from sys import stdin

input = stdin.readline

n,c = map(int, input().split())
points = [int(input()) for _ in range(n)]

points.sort()
def solv():
    left = 0
    right = points[-1]

    while left <= right:
        length = (left+right)//2

        before = points[0]
        cnt = 1
        for now in points[1:]:
            if now-before >= length:
                cnt += 1
                before = now

                if cnt > c:
                    break

        if cnt >= c:
            left = length+1
        else:
            right = length-1
    print(right)
solv()