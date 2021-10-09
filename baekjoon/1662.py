from sys import stdin

input = stdin.readline

input_data = input().strip()

def solv():
    stack = []

    cnt=0
    before=''
    for c in input_data:
        if c == '(':
            stack.append([cnt-1,before])
            cnt = 0
        elif c == ')':
            info = stack.pop()
            cnt = cnt*info[1]+info[0]
        else:
            cnt += 1
            before = int(c)
    print(cnt)
solv()