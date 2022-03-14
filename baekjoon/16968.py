fomatter = input()

candidate = set()

def solv():
    make_car_num(0,'')
    print(len(candidate))

def make_car_num(now, num):
    global candidate

    if now == len(fomatter):
        candidate.add(num)
        return

    if fomatter[now] == 'd':
        for target in range(10):
            if len(num) == 0 or num[-1] != str(target):
                make_car_num(now+1,num+str(target))

    else:
        for target in range(26):
            nxt = chr(ord('a')+target)
            if len(num) == 0 or num[-1] != nxt:
                make_car_num(now+1,num+nxt)

solv()