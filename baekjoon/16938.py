from itertools import combinations
n,l,r,x = map(int, input().strip().split())

level = list(map(int, input().strip().split()))

# level.sort()
# ans = 0
# def select_level(idx,sum_level,min_level,max_level):
#     if sum_level > r:
#         return
#
#     if sum_level >= l and max_level-min_level >= x:
#         global ans
#         ans += 1
#
#     if idx == n:
#         return
#     for i in range(idx, n):
#         select_level(i+1, sum_level+level[i], min(min_level, level[i]), max(max_level, level[i]))
#
# select_level(0,0,987654321,0)
# print(ans)

def solv():
    ans = 0
    for i in range(2,n+1):
        for comb in combinations(level,i):
            _sum = sum(comb)
            _min = min(comb)
            _max = max(comb)

            if l <= _sum <= r and _max-_min >= x:
                ans += 1
    return ans
print(solv())