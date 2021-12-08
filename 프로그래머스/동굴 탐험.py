from collections import deque


def solution(n, path, order):
    adj_list = set_adj_list(n, path)
    key, door = set_key_door(n, order)
    return bfs(n, adj_list, key, door)


def bfs(n, adj_list, key, door):
    wating = [False] * n
    visited = [False] * n
    q = deque([0])

    visited[0] = True
    count = 0
    if door[0]:
        return False
    if key[0] > 0:
        door[key[0]] = False
        key[0] = -1
    while q:
        q_len = len(q)
        flag = False
        for _ in range(q_len):
            now = q.pop()

            if key[now] > 0:
                door[key[now]] = False
                if wating[key[now]]:
                    wating[key[now]] = False
                    q.appendleft(key[now])
                    visited[key[now]] = True
                key[now] = -1

            flag = True
            count += 1
            for nxt in adj_list[now]:
                if not visited[nxt]:
                    if door[nxt]:
                        wating[nxt] = True
                    else:
                        visited[nxt] = True
                        q.appendleft(nxt)
        if not flag:
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
c = [[1, 0], [6, 7], [4, 1]]
print(solution(a,b,c))