from collections import deque


def solution(n, path, order):
    adj_list = set_adj_list(n, path)
    key, door = set_key_door(n, order)
    return bfs(n, adj_list, key, door)


def bfs(n, adj_list, key, door):
    visited = [False] * n
    q = deque([0])

    visited[0] = True
    count = 0

    if key[0] > 0:
        door[key[0]] = False
        key[0] = 0
    while q:
        q_len = len(q)
        flag = False
        for _ in range(q_len):
            now = q.pop()

            if door[now]:
                q.appendleft(now)
                continue

            if key[now] > 0:
                door[key[now]] = False
                key[now] = -1

            count += 1
            flag = True
            for nxt in adj_list[now]:
                if not visited[nxt]:

                    visited[nxt] = True
                    q.appendleft(nxt)
        if not flag or count == n:
            break
    return True if count == n else False


def set_key_door(n, order):
    key = [-1] * n
    door = [False] * n

    for a, b in order:
        key[a] = b
        door[b] = True
    return key, door


def set_adj_list(n, path):
    adj_list = [[] for _ in range(n)]
    for a, b in path:
        adj_list[a].append(b)
        adj_list[b].append(a)

    return adj_list
a = 9
b = [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
c = [[8, 5], [6, 7], [4, 1]]
print(solution(a,b,c))