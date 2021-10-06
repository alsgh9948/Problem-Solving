n = int(input())

prime_list = []

prime_check = [False]*4000001
for i in range(2,2001):
    if not prime_check[i]:
        for j in range(i*i, 4000001, i):
            prime_check[j] = True

for i in range(2,4000000):
    if prime_check[i]:
        continue
    prime_list.append(i)

start, end, temp_sum = 0,0,0

ans = 0
flag = False
while True:
    if temp_sum >= n:
        temp_sum -= prime_list[start]
        start += 1
    elif end >= len(prime_list):
        break
    else:
        temp_sum += prime_list[end]
        end += 1

    if temp_sum == n:
        ans += 1

    if end - start == 1 and temp_sum >= n:
        break
print(ans)