from sys import stdin

input = stdin.readline

n = int(input())
requests = list(map(int, input().split()))
total = int(input())

def solv():
    left,right = 1,max(requests)

    while left <= right:
        mid = (left+right)//2

        if is_possible(mid):
            left = mid+1
        else:
            right = mid-1
    print(right)

def is_possible(target):
    tmp = 0
    for request in requests:
        if request >= target:
            tmp += target
        else:
            tmp += request
    return tmp <= total

solv()