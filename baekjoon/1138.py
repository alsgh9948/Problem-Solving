n = int(input())
cnt = list(map(int, input().split()))

def solv():
    answer = [0]*n
    for i in range(n):
        for j in range(n):
            if cnt[i] == 0 and answer[j] == 0:
                answer[j] = i+1
                break
            elif answer[j] == 0:
                cnt[i] -= 1
    print(*answer)
solv()