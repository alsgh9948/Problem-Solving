from collections import defaultdict, deque

answer = []

def solution(tickets):
    global target_count
    target_count = len(tickets)
    set_adj_list(tickets)
    dfs('ICN', 0)
    return answer


def dfs(now, cnt):
    if cnt == target_count:
        set_answer()
        return True

    for _ in range(len(adj_list[now])):
        nxt = adj_list[now].pop()
        visited[now].appendleft(nxt)
        if dfs(nxt, cnt + 1):
            return True
        visited[now].popleft()
        adj_list[now].appendleft(nxt)
    return False


def set_answer():
    global answer
    answer.append('ICN')
    if visited['ICN']:
        nxt = visited['ICN'].pop()
        while nxt in visited and visited[nxt]:
            answer.append(nxt)
            nxt = visited[nxt].pop()
    answer.append(nxt)


def set_adj_list(tickets):
    global adj_list, visited
    adj_list = defaultdict(list)
    visited = {}
    for a, b in tickets:
        adj_list[a].append(b)

    for key in adj_list:
        adj_list[key] = deque(sorted(adj_list[key],reverse=True))
        visited[key] = deque()

a = [["ICN","ICN"]]
print(solution(a))