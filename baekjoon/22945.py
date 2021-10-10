from sys import stdin

input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))

def solv():
    left = 0
    right = n-1
    answer = -1
    while left < right:
        tmp = (right-left-1)*(nums[left] if nums[left] < nums[right] else nums[right])
        answer = tmp if tmp > answer else answer

        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    print(answer)
solv()