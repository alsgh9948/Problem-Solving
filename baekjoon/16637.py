n = int(input())
str = input().strip()

ans = -2**31


def solv(idx, rst):
    if idx >= n:
        global ans
        ans = max(ans, rst)
        return

    if idx + 3 < n and str[idx+2] == '*':
        solv(idx + 4, calc(rst, str[idx], calc(str[idx + 1], str[idx + 2], str[idx + 3])))
    else:
        solv(idx+2, calc(rst,str[idx], str[idx+1]))
    if idx+3 < n:
        solv(idx+4, calc(rst,str[idx], calc(str[idx+1],str[idx+2],str[idx+3])))


def calc(a, op, b):
    a = int(a)
    b = int(b)
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    else:
        return a*b


solv(1, int(str[0]))
solv(3, calc(int(str[0]), str[1], str[2]))
print(ans)