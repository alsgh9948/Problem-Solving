from sys import stdin

input = stdin.readline

n,m = map(int, input().split())
infos = [list(input().strip().split()) for _ in range(n)]

def solv():
    for _ in range(m):
        target = int(input())
        location = binary_search(target)
        print(infos[location][0])

def binary_search(target):
    left = 0
    right = n-1

    while left <= right:
        mid = (left+right)//2

        if int(infos[mid][1]) < target:
            left = mid+1
        else:
            right = mid-1
    return left
solv()