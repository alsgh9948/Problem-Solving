from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())
cnt = [[0,0] for _ in range(101)]

def solv():
    global cnt
    nums = list(map(int,input().split()))

    candidate = []
    t = 1
    for num in nums:
        if cnt[num][0] == 0:
            if len(candidate) == n:
                candidate = renew_candidate(candidate)
            candidate.append(num)
            cnt[num][0] += 1
            cnt[num][1] = t
        else:
            cnt[num][0] += 1
        t += 1
    candidate.sort()
    print(*candidate)
def renew_candidate(candidate):
    global cnt
    tmp = []
    for num in candidate:
        tmp.append((cnt[num][0],cnt[num][1],num))
    tmp = sorted(tmp, key = lambda x:(-x[0],-x[1]))

    candidate = []
    for a,b,num in tmp[:n-1]:
        candidate.append(num)

    cnt[tmp[-1][2]] = [0,0]
    return candidate

solv()