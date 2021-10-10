from sys import stdin

input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
def solv():
    left = 0
    right = n-1
    target = 98765432100
    answer_left = 0
    answer_right = n-1
    while left < right:
        tmp = nums[left]+nums[right]
        if abs(tmp) < target:
            target = abs(tmp)
            answer_left,answer_right = left,right
        if tmp > 0:
            right -= 1
        elif tmp < 0:
            left += 1
        else:
            break
    print(nums[answer_left],nums[answer_right])
solv()