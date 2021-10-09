n,m = map(int, input().strip().split())
num_list = list(map(int, input().split()))
start, end = 0,0
ans = 0
temp_sum = 0
while True:
    if temp_sum >= m:
        temp_sum -= num_list[start]
        start += 1
    elif end == n:
        break
    else:
        temp_sum += num_list[end]
        end += 1
    if temp_sum == m:
        ans += 1

print(ans)
