n = int(input())

def solv():
    make_nums([],0)
def make_nums(select,cnt):
    if cnt == n:
        print(''.join(select))
        return True
    for num in '123':
        select.append(num)
        flag = True
        step = 1
        for idx in range(cnt-1,-1,-1):
            if select[idx] == num:
                if ''.join(select[idx+1-step:idx+1]) == ''.join(select[idx+1:]):
                    flag = False
                    break
            step += 1
            if step > (cnt+1)//2:
                break
        if flag:
            if make_nums(select,cnt+1):
                return True
            else:
                select.pop()
        else:
            select.pop()
    return False

solv()