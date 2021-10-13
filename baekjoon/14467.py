n = int(input())

cow = [-1]*11
answer = 0
for _ in range(n):
    a,b = map(int, input().split())
    if cow[a] != b:
        if cow[a] == -1:
            cow[a] = b
        else:
            cow[a] ^= 1
            answer += 1

print(answer)