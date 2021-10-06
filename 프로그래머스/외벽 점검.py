from itertools import permutations
INF = 9876543210

def solution(input_n, input_weak, input_dist):
    global answer, dist, weak, n, m
    n = input_n
    weak = input_weak
    dist = input_dist
    m = len(weak)

    answer = INF
    remain = len(weak)

    for order in permutations(dist,len(dist)):
        for start in range(m):
            visited = [False]*n
            check_weak(start, 0, order, visited, 0, remain)
    return answer if answer != INF else -1


def check_weak(start, now, order, visited, ans, remain):
    global answer, weak
    if ans >= answer:
        return
    if remain == 0:
        answer = min(answer, ans)
        return

    if now == len(order):
        return

    w = weak[start]
    visited[w] = True
    cnt = 1
    end = start
    for _ in range(m):
        end = (end+1)%m
        if not is_possible(w,weak[end],order[now]) or visited[weak[end]]:
            break
        else:
            visited[weak[end]] = True
            cnt += 1
    check_weak(end,now+1,order,visited,ans+1,remain-cnt)
def is_possible(start,end,max_dist):
    if end - start < 0:
        if n - start + end <= max_dist:
            return True
        else:
            return False
    else:
        if end - start <= max_dist:
            return True
        else:
            return False

# a = 200
a = 130
b = [0,10,30,50,100,120]
# b = [1, 5, 6, 10]
# b = [0, 10, 50, 80, 120, 160]
c = [5,10,50,100]
# c = [4,3,2,1]
# c = [1, 10, 5, 40, 30]
print(solution(a,b,c))