from sys import stdin

input = stdin.readline
n,m = map(int, input().strip().split())
nums = list(map(int, input().split()))

def solv():
    left=right=0
    tmp = 0
    answer = 0
    while right < n:
        if tmp >= m:
            tmp -= nums[left]
            left += 1
        elif tmp < m:
            tmp += nums[right]
            right += 1

        if tmp == m:
            answer += 1
    print(answer)

solv()