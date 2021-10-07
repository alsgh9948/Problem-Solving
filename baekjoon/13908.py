n,m = map(int, input().split())

if m != 0:
    answer = 0
    nums = input().split()
    for target in range(10 ** n):
        flag = True
        str_num = str(target).zfill(n)
        for num in nums:
            if num not in str_num:
                flag = False
        if flag:
            answer += 1
    print(answer)
else:
    print(10**n)