from sys import stdin
from collections import deque
from itertools import combinations

input = stdin.readline

n = int(input())
count = list(map(int, input().split()))

adj_list = [[] for _ in range(n)]
zero_count = 0
for i in range(n):
    input_data = list(map(int, input().split()))
    if input_data[0] == 0:
        zero_count += 1
    for num in input_data[1:]:
        adj_list[i].append(num-1)

def solv():
    answer = 9876543210
    for cnt in range(1,n):
        for member in combinations(range(1,n),cnt):
            a_group = [0]
            b_group = []
            a_sum = count[0]
            b_sum = 0
            for target in range(1,n):
                if target in member:
                    b_group.append(target)
                    b_sum += count[target]
                else:
                    a_group.append(target)
                    a_sum += count[target]

            if check_group(a_group) and check_group(b_group):
                answer = min(answer, abs(a_sum-b_sum))

    print(answer)
def check_group(group):
    visited = bfs(group)
    for num in group:
        if not visited[num]:
            return False
    return True

def bfs(group):
    visited = [False]*n

    start = group[0]
    visited[start] = True

    q = deque([start])

    while q:
        now = q.pop()

        for nxt in adj_list[now]:
            if not visited[nxt] and nxt in group:
                visited[nxt] = True
                q.appendleft(nxt)

    return visited

if n == 2:
    print(abs(count[0]-count[1]))
elif zero_count >= 2:
    print(-1)
else:
    solv()