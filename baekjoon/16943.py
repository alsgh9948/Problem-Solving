from itertools import permutations

a,b = input().strip().split()

a = list(map(int,a))
a.sort()

b = int(b)
ans = -1
for perm in permutations(a,len(a)):
    num = 0
    for n in perm:
        num = num*10 + n
        if num > b or num == 0:
            num = -1
            break
    ans = max(ans, num)
print(ans)
