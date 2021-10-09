n,m = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
def select_num(cnt,select):
    global answer
    if cnt == n:
        for num in nums:
            if num not in select:
                return
        answer += 1
        return

    for num in range(10):
        select_num(cnt+1,select+[num])

select_num(0,[])
print(answer)