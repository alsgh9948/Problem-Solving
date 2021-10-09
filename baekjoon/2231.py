from sys import stdin

input = stdin.readline

a,p = map(int, input().split())

nums = [a]
def solv():
    new_num = a
    while True:
        new_num = calc_num(new_num)
        idx = check_num(new_num)
        if idx != -1:
            print(idx)
            return
        nums.append(new_num)

def calc_num(n):
    new_num = 0
    while n != 0:
        new_num += (n%10)**p
        n //= 10
    return new_num

def check_num(n):
    for idx in range(len(nums)):
        if n == nums[idx]:
            return idx
    return -1

solv()