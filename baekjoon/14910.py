from sys import stdin

input = stdin.readline

nums = list(map(int, input().split()))

def solv():
    before = nums[0]
    for num in nums[1:]:
        if before > num:
            print('Bad')
            return
        before = num
    print('Good')

solv()