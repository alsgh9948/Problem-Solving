from itertools import combinations

n = int(input())
nums = list(map(int, input().split()))

def solv():
    used = set()
    used.add(0)
    for cnt in range(1,n+1):
        for comb in combinations(nums,cnt):
            used.add(sum(comb))
    used = sorted(used)
    for i in range(len(used)):
        if used[i] != i:
            print(i)
            break
    else:
        print(used[-1]+1)
solv()