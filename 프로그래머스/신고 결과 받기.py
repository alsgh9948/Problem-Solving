from collections import defaultdict
def solution(id_list, report, k):
    idx = {id_list[i]:i for i in range(len(id_list))}
    report_info = defaultdict(set)

    for data in report:
        a,b = data.split()
        report_info[b].add(a)

    answer = [0]*len(id_list)
    for id in id_list:
        if len(report_info[id]) >= k:
            for target in report_info[id]:
                answer[idx[target]] += 1

    return answer
a = ["muzi", "frodo", "apeach", "neo"]
b = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
c = 2

print(solution(a,b,c))