def solution(input_info, query):
    answer = []

    info = init_info(input_info)

    for key in info:
        info[key].sort()

    for q in query:
        split_q = q.split(" and ")
        score_q = split_q[-1].split()
        key, score = ''.join(split_q[:-1]) + score_q[0], int(score_q[1])

        idx = binary_search(score, key, info)
        if idx != -1:
            answer.append(len(info[key]) - idx)
    return answer


def binary_search(target, key, info):
    left = 0
    right = len(info[key])-1

    while left < right:
        mid = (left + right) // 2
        if info[key][mid] >= target:
            right = mid
        else:
            left = mid+1
    return left


def init_info(input_info):
    info = {}
    for a in ["cpp", "java", "python", "-"]:
        for b in ["backend", "frontend", "-"]:
            for c in ["junior", "senior", "-"]:
                for d in ["chicken", "pizza", "-"]:
                    info[a + b + c + d] = []

    for data in input_info:
        split_data = data.split()
        score = int(data.split()[-1])
        for a in [split_data[0], "-"]:
            for b in [split_data[1], "-"]:
                for c in [split_data[2], "-"]:
                    for d in [split_data[3], "-"]:
                        key = a + b + c + d
                        info[key].append(score)
    return info

a = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
b = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
print(solution(a,b))