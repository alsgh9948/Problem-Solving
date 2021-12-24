from sys import stdin

input = stdin.readline

n,k = map(int, input().split())
nums = list(map(int, input().split()))

def solv():
    left=right=0
    count = [0]*(max(nums)+1)
    answer = 0
    while right < n:
        right_num = nums[right]
        left_num = nums[left]
        if count[right_num] < k:
            count[right_num] += 1
            right += 1
        else:
            count[left_num] -= 1
            left += 1

        answer = answer if right-left < answer else right-left
    print(answer)
solv()