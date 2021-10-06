import sys

n = int(sys.stdin.readline())

schedule = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = -1
def solv(now, sum, temp_price):
    if now >= len(schedule):
        global ans
        if now == len(schedule):
            sum += temp_price
        ans = max(ans, sum)

        return
    solv(now + schedule[now][0], sum+temp_price, schedule[now][1])
    solv(now + 1, sum+temp_price, 0)

    return

solv(0,0,0)

print(ans)

