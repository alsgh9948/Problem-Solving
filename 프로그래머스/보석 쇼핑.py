def solution(gems):
    gem_info = set_gems_info(gems)
    return calc_length(gem_info, gems)

def calc_length(gem_info, gems):
    left = right = 0
    length = 9876543210
    answer = []

    count = 0
    target_count = len(gem_info)
    while left < len(gems):
        if right < len(gems) and count < target_count:
            gem = gems[right]
            if gem_info[gem] == 0:
                count += 1
            gem_info[gem] += 1
            right += 1
            if count == target_count:
                length,answer = check_answer(answer,length,left,right)

        else:
            gem = gems[left]
            gem_info[gem] -= 1
            if gem_info[gem] == 0:
                count -= 1
            left += 1
            if count == target_count:
                length,answer = check_answer(answer,length,left,right)
    return answer

def check_answer(answer,length,left,right):
    sub = right - left
    if sub < length:
        return sub, [left + 1, right]
    return length,answer
def set_gems_info(gems):
    gem_info = {}

    for gem in set(gems):
        gem_info[gem] = 0

    return gem_info

a = ["DIA", "EM", "EM", "RUB", "DIA"]
print(solution(a))