from sys import stdin
from itertools import combinations

input = stdin.readline

h,w = map(int, input().split())
n = int(input())

points = []
for _ in range(n):
    points.append(list(map(int, input().split())))

def solv():
    answer = 0
    for a,b in combinations(points, 2):
        x1,y1 = a
        x2,y2 = b

        if point_validator(x1,y1,x2,y2):
            answer = max(answer,x1*y1+x2*y2)
    print(answer)

def point_validator(x1,y1,x2,y2):
    if y1+y2 <= w and max(x1,x2) <= h:
        return True
    elif y1+y2 <= h and max(x1,x2) <= w:
        return True
    elif y1+x2 <= w and max(x1,y2) <= h:
        return True
    elif y1+x2 <= h and max(x1,y2) <= w:
        return True
    elif x1+y2 <= w and max(y1,x2) <= h:
        return True
    elif x1+y2 <= h and max(y1,x2) <= w:
        return True
    elif x1+x2 <= w and max(y1,y2) <= h:
        return True
    elif x1+x2 <= h and max(y1,y2) <= w:
        return True
    return False

solv()