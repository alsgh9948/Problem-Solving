from sys import stdin

input = stdin.readline

k,n = map(int,input().split())

lan_cable = []
max_lan_cable = 0
for _ in range(k):
    lan_cable.append(int(input().strip()))
    max_lan_cable = max(max_lan_cable, lan_cable[-1])

def solv():
    left = 1
    right = max_lan_cable
    while left <= right:
        cut_length = (left+right)//2

        cnt = 0
        for lan in lan_cable:
            cnt += lan//cut_length
            if cnt >= n:
                break

        if cnt >= n:
            left = cut_length + 1
        else:
            right = cut_length - 1
    return right

print(solv())