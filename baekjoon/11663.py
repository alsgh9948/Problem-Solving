from sys import stdin

input = stdin.readline

n,m = map(int, input().split())
points = list(map(int, input().split()))
points.sort()

def solv():
    for _ in range(m):
        a,b = map(int, input().split())

        l = binary_search(a,'l')
        r = binary_search(b,'r')
        if l == r:
            print(0)
        else:
            print(r-l)

def binary_search(target,typ):
    left,right = 0,n-1
    while left <= right:
        mid = (left+right)//2

        if typ == 'l' and points[mid] >= target:
            right = mid - 1
        elif typ == 'r' and points[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left
solv()