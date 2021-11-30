def solution(tickets):
    global target_count
    target_count = len(tickets)
    answer = []
    set_index(tickets)

    answer = dfs(airport_index['ICN'], 0, 0)
    return answer


def dfs(now, count, visited_count):
    global visited
    if count == target_count:
        if visited_count == target_count:
            return [index_airport[now]]
        else:
            return None
    elif count > target_count:
        return None

    for nxt in adj_list[now]:
        if visited[now][nxt] != 0:
            visited[now][nxt] -= 1
            result = dfs(nxt, count + 1, visited_count + 1)
            if result:
                return [index_airport[now]] + result
            visited[now][nxt] += 1
        else:
            result = dfs(nxt, count + 1, visited_count)
            if result:
                return [index_airport[now]] + result


def set_index(tickets):
    global airport_index, index_airport, adj_list, visited
    airport = set()
    for a, b in tickets:
        airport.add(a)
        airport.add(b)

    airport = sorted(airport)
    airport_index = {}
    index_airport = []
    for name in airport:
        index_airport.append(name)
        airport_index[name] = len(airport_index)

    adj_list = [[] for _ in range(len(airport))]
    visited = [[0] * len(airport_index) for _ in range(len(airport_index))]
    for a, b in tickets:
        adj_list[airport_index[a]].append(airport_index[b])
        visited[airport_index[a]][airport_index[b]] += 1
    for idx in range(len(adj_list)):
        adj_list[idx].sort()
a = [["ICN", "A"], ["ICN", "A"], ["A", "ICN"]]
b = ["ICN", "A", "ICN", "A"]
print(solution(a))