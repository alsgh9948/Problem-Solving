from sys import stdin

input = stdin.readline

d,n = map(int, input().split())
size = [9876543210]+list(map(int, input().split()))
height = list(map(int, input().split()))


def solv():
    for idx in range(2,d+1):
        if size[idx-1] <= size[idx]:
            size[idx] = size[idx-1]

    idx = d
    for h in height:
        while size[idx] < h:
            idx -= 1
        idx -= 1

        if idx <= 0:
            idx = -1
            break
    print(idx+1)
solv()