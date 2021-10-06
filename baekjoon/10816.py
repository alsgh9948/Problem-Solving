from sys import stdin
input = stdin.readline
n = int(input())

card = {}
for num in input().split():
    if num in card:
        card[num] += 1
    else:
        card[num] = 1

m = int(input())

ans = []
for target in input().split():
    if target in card:
        ans.append(card[target])
    else:
        ans.append(0)

print(*ans)
