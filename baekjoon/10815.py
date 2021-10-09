from sys import stdin

input = stdin.readline

n = int(input())
num = set((map(int, input().split())))

m = int(input())
target = list(map(int, input().split()))

def solv():
    ans = []
    for t in target:
        if t in num:
            ans.append(1)
        else:
            ans.append(0)

    print(*ans)

solv()