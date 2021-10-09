def solution(food_times, k):
    answer = 0
    num_count = set_num_count(food_times)
    total = len(food_times)

    start = 0
    for idx in range(len(num_count)):
        t, info = num_count[idx]
        sub = t - start

        if k - total * sub == 0:
            idx = (idx + 1) % len(num_count)
            return food_times.index(num_count[idx][1]['pos'][0])
        elif k - total * sub < 0:
            return check_answer(k, idx, num_count)
        else:
            k -= total * sub
            total -= info['cnt']
            start = t
    return -1


def check_answer(k, start, num_count):
    for idx in range(start, len(num_count)):
        t, info = num_count[idx]

        if k - info['cnt'] <= 0:
            return info['pos'][k-1]
        else:
            k -= info['cnt']
def set_num_count(food_times):
    num_count_dict = {}

    idx = 1
    for t in food_times:
        if t in num_count_dict:
            num_count_dict[t]['cnt'] += 1
            num_count_dict[t]['pos'].append(idx)
        else:
            num_count_dict[t] = {
                'cnt': 1,
                'pos': [idx]
            }
        idx += 1
    num_count = sorted(list(num_count_dict.items()))
    return num_count

a = [4, 2, 3, 6, 7, 1, 5, 8]
b = 16
print(solution(a,b))