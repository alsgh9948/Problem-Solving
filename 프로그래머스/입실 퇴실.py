def solution(enter, leave):
    locations = [0] * (len(enter) + 1)
    origin_locations = [0] * (len(enter) + 1)
    for idx in range(len(enter)):
        locations[enter[idx]] = idx
        origin_locations[enter[idx]] = idx

    answer = [0] * (len(enter) + 1)
    for num in leave:
        end = locations[num]
        origin_end = origin_locations[num]
        for target in enter[:end]:
            if num == target:
                continue
            if target != -1:
                answer[num] += 1
                answer[target] += 1
                locations[target] = end
        enter[origin_end] = -1
    return answer[1:]

a = [1, 4, 2, 3]
b = [2, 1, 3, 4]
print(solution(a,b))