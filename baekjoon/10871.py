n,x = map(int, input().split())
nums = list(int(a) for a in input().split() if int(a)<x)
print(*nums)
