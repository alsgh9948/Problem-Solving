from sys import stdin

input = stdin.readline

n,m,l = map(int, input().split())

locations = [0]
if n > 0:
    locations.extend(list(map(int, input().split())))
locations.sort()
locations.append(l)
def solv():
    left = 1
    right = l-1

    while left <= right:
        mid = (left+right)//2

        if is_possible(mid):
            right = mid-1
        else:
            left = mid+1
    print(left)

def is_possible(length):
    count = 0
    for a,b in zip(locations[:-1],locations[1:]):
        count += (b-a-1)//length
    return count <= m
solv()