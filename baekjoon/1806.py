n,s = map(int,input().strip().split())

num_list = list(map(int,input().strip().split()))
start,end = 0,0
temp_sum = 0
ans = 100001
len_temp = 0
while True:
    if temp_sum >= s:
        if len_temp < ans:
            ans = len_temp
        else:
            temp_sum -= num_list[start]
            start += 1
            len_temp -= 1
    elif end == n:
        break
    else:
        temp_sum += num_list[end]
        end += 1
        len_temp += 1
print(ans if ans != 100001 else 0)