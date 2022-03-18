max_score = -1


def solution(input_n, input_info):
    global n, apeach_info, answer
    n = input_n
    apeach_info = input_info

    answer = []
    select(0, [0] * 11, 0, n)
    if max_score == -1:
        return [-1]
    return answer


def select(now, lion_info, lion_score, remain):
    if now == 11 or remain == 0:
        if remain != 0:
            lion_info[10] += remain

        calc_score(lion_info)

        if remain != 0:
            lion_info[10] = 0
        return

    if apeach_info[now] + 1 <= remain:
        cnt = apeach_info[now] + 1
        lion_info[now] = cnt
        select(now + 1, lion_info, lion_score + 10-now, remain - cnt)
        lion_info[now] = 0
    select(now + 1, lion_info, lion_score, remain)


def calc_score(lion_info):
    global max_score, answer
    lion, apeach = 0, 0

    for idx in range(10):
        if lion_info[idx] > apeach_info[idx]:
            lion += 10 - idx
        elif apeach_info[idx] != 0:
            apeach += 10 - idx
    if lion <= apeach:
        return

    score = lion - apeach
    if max_score < score:
        max_score = score
        answer = [i for i in lion_info]
    elif max_score == score:
        for idx in range(10, -1, -1):
            if answer[idx] > lion_info[idx]:
                return
            elif answer[idx] < lion_info[idx]:
                answer = [i for i in lion_info]
                return
