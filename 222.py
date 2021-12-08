from collections import deque


def solution(arr, x):
    # Write your code here
    arr.sort()
    max_num = arr[-1]
    used = [False] * (max_num + x+1)
    for num in arr:
        used[num] = True

    targets = []
    for num in range(max_num + x+1):
        if not used[num]:
            targets.append(num)

    for num in arr:
        q = deque(targets)
        targets = []
        q_len = len(q)

        for _ in range(q_len):
            target = q.popleft()
            if num == target or target % x == num % x:
                break
            else:
                targets.append(target)
        else:
            return targets[0]

        targets.extend(q)

# print(solution([0,1,2,2,0,0,10,3],3))
print(solution([1,3,4],2))