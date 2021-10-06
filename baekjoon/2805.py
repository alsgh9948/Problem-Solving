from sys import stdin
input = stdin.readline

n,m = map(int, input().split())
woods = list(map(int, input().split()))
large_wood = max(woods)

def solv():
    left = 0
    right = large_wood

    while left <= right:
        cut_length = (left+right)//2

        total = 0
        for wood in woods:
            total += wood-cut_length if wood >= cut_length else 0
            if total >= m:
                break

        if total < m:
            right = cut_length - 1
        else:
            left = cut_length + 1
    return right
print(solv())

