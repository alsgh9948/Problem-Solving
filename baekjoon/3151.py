from sys import stdin

input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
def solv():
    answer = 0
    for target in range(n-2):
        answer += search_num(target)
    print(answer)
def search_num(target):
    cnt = 0
    target_sum = -nums[target]
    left = target+1
    right = n-1
    before = n
    while left < right:
        tmp = nums[left]+nums[right]
        if tmp == target_sum:
            if nums[left] == nums[right]:
                cnt += right-left
            else:
                if before > right:
                    before = right
                    while before >= 0 and nums[right] == nums[before-1]:
                        before -= 1
                cnt += right-before+1
            left += 1
        elif tmp > target_sum:
            right -= 1
        else:
            left += 1
    return cnt
solv()