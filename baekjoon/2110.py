from sys import stdin
input = stdin.readline

n,c = map(int, input().split())

wifi = []
for _ in range(n):
    wifi.append(int(input()))

wifi.sort()
def solv():
    left = 0
    right = wifi[n-1]

    while left <= right:
        length = (left+right)//2

        start = wifi[0]
        cnt = 1
        for end in wifi:
            if end - start >= length:
                cnt += 1
                start = end

            if cnt > c:
                break
        if cnt < c:
            right = length - 1
        else:
            left = length + 1
    return right

print(solv())