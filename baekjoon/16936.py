n = int(input())
num = list(map(int,input().split()))

def dfs(now,visited):
    if len(visited) == len(num):
        print(*visited)
        return True

    if now%3==0 and now//3 not in visited and now//3 in num:
        visited.append(now // 3)
        if dfs(now//3, visited):
            return True
        visited.pop()

    if now*2 not in visited and now*2 in num:
        visited.append(now * 2)
        if dfs(now*2, visited):
            return True
        visited.pop()

for start in num:
    if dfs(start,[start]):
        break

