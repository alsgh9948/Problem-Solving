def solution(play_time, adv_time, logs):
    global sec_arr, play_time_sec, adv_time_sec

    play_time_sec = convert_time_to_sec(play_time.split(':')) + 1
    adv_time_sec = convert_time_to_sec(adv_time.split(':'))

    sec_arr = [0] * (play_time_sec)
    set_sec_arr(logs)
    return search_start_time()

def search_start_time():
    start = 0
    ans_cnt = cnt = sum(sec_arr[:adv_time_sec])
    ans_str = 0
    for end in range(adv_time_sec, play_time_sec):
        cnt -= sec_arr[start]
        start += 1
        cnt += sec_arr[end]

        if ans_cnt < cnt:
            ans_cnt = cnt
            ans_str = start
    return convert_sec_to_time(ans_str)
def set_sec_arr(logs):
    global sec_arr
    for log in logs:
        start = convert_time_to_sec(log[:8].split(':'))
        end = convert_time_to_sec(log[9:].split(':'))
        sec_arr[start] += 1
        sec_arr[end] -= 1

    for idx in range(1, play_time_sec):
        sec_arr[idx] += sec_arr[idx - 1]

def convert_time_to_sec(t):
    h = 60 * 60 * int(t[0])
    m = 60 * int(t[1])
    c = int(t[2])

    return h + m + c
def convert_sec_to_time(sec):
    h = sec // (60 * 60)
    sec %= (60 * 60)
    m = sec // 60
    sec %= 60
    s = sec
    return '%02d:%02d:%02d' % (h, m, s)
a = "00:00:10"
b = "00:00:10"
c = ["00:00:02-00:00:03", "00:00:03-00:00:04", "00:00:06-00:00:08", "00:00:05-00:00:07", "00:00:05-00:00:07"]
print(solution(a,b,c))