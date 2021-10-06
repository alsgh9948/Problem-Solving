from sys import stdin

input = stdin.readline

input_data = input().strip()

def solv():
    s = []
    for c in input_data:
        if c in '([':
            s.append(c)
        elif s:
            if c == ')':
                if s[-1] == '(':
                    s.pop()
                    s.append(2)
                elif s[-1] == '[':
                    print(0)
                    return
                else:
                    s.append(sum_num(s,'(',2))
            else:
                if s[-1] == '[':
                    s.pop()
                    s.append(3)
                elif s[-1] == '(':
                    print(0)
                    return
                else:
                    s.append(sum_num(s,'[',3))
        else:
            print(0)
            return

    answer = 0
    for c in s:
        if c in ['(',')','[',']']:
            print(0)
            return
        else:
            answer += c
    print(answer)
def sum_num(s,target,op):
    rst = 0
    while s and s[-1] not in ['(',')','[',']']:
        rst += s.pop()
    if s and s[-1] == target:
        s.pop()
        return rst*op
    else:
        return 0

solv()