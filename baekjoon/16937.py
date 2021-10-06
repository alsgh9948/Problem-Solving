from itertools import combinations

h,w = map(int, input().strip().split())
n = int(input().strip())

s = []
board = [[False]*w for _ in range(h)]
for _ in range(n):
    r,c = map(int, input().strip().split())
    s.append((r,c))

def solv():
    ans = 0
    for comb in combinations(s,2):
        a,b = comb

        if a[0]+b[0] <= h and max(a[1],b[1]) <= w:
            ans = max(ans, a[0] * a[1] + b[0] * b[1])
        elif a[0]+b[1] <= h and max(a[1],b[0]) <= w:
            ans = max(ans, a[0] * a[1] + b[0] * b[1])
        elif a[1] + b[0] <= h and max(a[0],b[1]) <= w:
            ans = max(ans, a[0] * a[1] + b[0] * b[1])
        elif a[1]+b[1] <= h and max(a[0],b[0]) <= w:
            ans = max(ans, a[0] * a[1] + b[0] * b[1])
        elif a[0]+b[0] <= w and max(a[1],b[1]) <= h:
            ans = max(ans, a[0] * a[1] + b[0] * b[1])
        elif a[0]+b[1] <= w and max(a[1],b[0]) <= h:
            ans = max(ans, a[0] * a[1] + b[0] * b[1])
        elif a[1] + b[0] <= w and max(a[0],b[1]) <= h:
            ans = max(ans, a[0] * a[1] + b[0] * b[1])
        elif a[1]+b[1] <= w and max(a[0],b[0]) <= h:
            ans = max(ans, a[0] * a[1] + b[0] * b[1])

    return ans

print(solv())