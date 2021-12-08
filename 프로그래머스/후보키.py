from itertools import combinations


def solution(relation):
    global n, used
    n = len(relation[0])
    used = []
    answer = 0

    for count in range(1, n + 1):
        for order in combinations(range(n), count):
            if is_used(order):
                continue
            if is_possible(order, relation):
                answer += 1
                used.append(order)
    return answer


def is_possible(order, relation):
    keys = set()

    for row in relation:
        key = ''
        for idx in order:
            key += '-' + row[idx]
        if key in keys:
            return False
        keys.add(key)

    return True


def is_used(order):
    for arr in used:
        count = 0
        for idx in arr:
            if idx in order:
                count += 1
        if count == len(arr):
            return True
    return False