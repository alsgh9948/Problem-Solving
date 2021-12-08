from sys import stdin

input = stdin.readline

n,m = map(int, input().split())
infos = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        infos.append((tmp[j],i))

infos.sort()
def solv():
    answer = 98765432100
    left=right=0

    count=0
    show_count = [0]*n

    show_count[infos[right][1]] += 1
    if show_count[infos[right][1]] == 1:
        count += 1
    else:
        count -= 1
    right += 1

    while right < m*n:
        if count == n:
            show_count[infos[left][1]] -= 1
            if show_count[infos[left][1]] == 0:
                count -= 1
            left += 1

        if count < n:
            show_count[infos[right][1]] += 1
            if show_count[infos[right][1]] == 1:
                count += 1
            right += 1

        if count == n:
            answer = min(answer, infos[right-1][0] - infos[left][0])

    print(answer)
solv()
