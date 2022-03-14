from sys import stdin
from itertools import combinations

input = stdin.readline

n,l,r,x = map(int, input().split())
arr = list(map(int, input().split()))

def solv():
    answer = 0
    for cnt in range(2,n+1):
        for problems in combinations(arr, cnt):
            total_score = sum(problems)
            max_score = max(problems)
            min_score = min(problems)

            if l <= total_score <= r and x <= max_score-min_score:
                answer += 1

    print(answer)

solv()