n = int(input())
answer = 0
while n >= 0:
    if n%5 == 0:
        print(answer+n//5)
        break
    else:
        n -= 3
        answer += 1
else:
    print(-1)