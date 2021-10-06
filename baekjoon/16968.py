from itertools import product
num = [i for i in range(10)]
alpha = [i for i in range(26)]

str = input().strip()

def calc_cnt(typ,cnt):
    if cnt <= 2:
        if typ == 'd':
            start = 10
        else:
            start = 26
        if cnt == 0:
            return 0
        rst = 1
        for i in range(start, start - cnt, -1):
            rst *= i
        return rst
    else:
        rst = 0
        target = num if typ == 'd' else alpha
        for perm in product(target,repeat=cnt):
            flag = True
            for idx in range(cnt-1):
                if perm[idx] == perm[idx+1]:
                    flag = False
                    break
            if flag:
                rst += 1
        return rst

ans = 1
c = str[0]
cnt = 1
for i in range(1,len(str)):
    if c != str[i]:
        ans *= calc_cnt(c,cnt)
        cnt = 1
        c = str[i]
    else:
        cnt += 1
ans *= calc_cnt(c,cnt)
print(ans)