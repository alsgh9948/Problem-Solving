n = input().strip()

min_answer = 9876543210
max_answer = 0
def solv():
    go(n,0)
    print(min_answer,max_answer)
def go(nums,cnt):
    global min_answer,max_answer
    if len(nums) == 1:
        if nums in '13579':
            cnt += 1
        min_answer = min(min_answer, cnt)
        max_answer = max(max_answer, cnt)
        return
    if len(nums) == 2:
        for idx in range(1,len(nums)):
            a,a_cnt = list_to_int(nums[:idx])
            b,b_cnt = list_to_int(nums[idx:])
            go(str(int(a)+int(b)),cnt+a_cnt+b_cnt)
    else:
        for idx1 in range(1,len(nums)-1):
            for idx2 in range(idx1+1,len(nums)):
                a,a_cnt = list_to_int(nums[:idx1])
                b,b_cnt = list_to_int(nums[idx1:idx2])
                c,c_cnt = list_to_int(nums[idx2:])
                go(str(a+b+c),cnt+a_cnt+b_cnt+c_cnt)
def list_to_int(nums):
    rst = 0
    cnt = 0
    for num in nums:
        if num in '13579':
            cnt += 1
        rst = rst*10+int(num)
    return rst, cnt
solv()