from sys import stdin

input = stdin.readline

n = int(input())
arr = []
target = {}
arr = list(map(int, input().split()))

for num in arr:
    target[num] = -1

def solv():
    global target
    for start in target.keys():
        target[start] = 0
        if dfs(start, 1):
            print_answer(start)
            return
        target[start] = -1


def print_answer(start):
    now = start
    while target[now] != -2:
        print(now, end=' ')
        now = target[now]
    print(now)
def dfs(now, cnt):
    global target
    if cnt == n:
        target[now] = -2
        return True

    if now%3 == 0 and now//3 in target and target[now//3] == -1:
        target[now] = now//3
        if dfs(now//3, cnt+1):
            return True
        target[now] = -1

    if now*2 in target and target[now*2] == -1:
        target[now] = now*2
        if dfs(now*2,cnt+1):
            return True
        target[now] = -1

    return False

solv()