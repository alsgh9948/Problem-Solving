from sys import stdin

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()

ans = 0
for idx in range(n):
    ans += a[idx]*b[idx]
print(ans)