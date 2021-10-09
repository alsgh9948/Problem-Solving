num_list = list(map(int, input().split()))

def solv():
    min_num = calc_clock_num()
    clock_num = set_clock_num(min_num)
    ans = 1

    for num in range(1111,min_num):
        if clock_num[num]:
            ans += 1
    print(ans)

def calc_clock_num():
    nums = []
    for idx in range(4):
        n = 0
        for i in range(4):
            n = n*10+num_list[(idx+i)%4]
        nums.append(n)
    return min(nums)
def set_clock_num(min_num):
    clock_num = [False]*(min_num+1)
    for num in range(1111, min_num):
        num_list = list(map(int, str(num)))
        nums = []
        for idx in range(4):
            n = 0
            for i in range(4):
                n = n * 10 + num_list[(idx + i) % 4]
            nums.append(n)
        clock_num[min(nums)] = True
    return clock_num

solv()