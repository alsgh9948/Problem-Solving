from sys import stdin

n,m = map(int, stdin.readline().split())

friends = [[] for _ in range(n)]
friends_count = [0]*n
for _ in range(m):
    a,b = map(int, input().split())
    friends[a-1].append(b-1)
    friends[b-1].append(a-1)
    friends_count[a-1] += 1
    friends_count[b-1] += 1

def solv():
    answer = 9876543210
    for i in range(n):
        if friends_count[i] >= 2:
            for j in range(friends_count[i]):
                a = friends[i][j]
                for k in range(j+1,friends_count[i]):
                    b = friends[i][k]
                    if b in friends[a]:
                       answer = min(answer,(friends_count[i]+friends_count[a]+friends_count[b]-6))
    print(answer if answer != 9876543210 else -1)
solv()