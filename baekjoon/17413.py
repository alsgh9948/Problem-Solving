from sys import stdin

input = stdin.readline

input_data = list(input().strip())

def solv():
    answer = ''
    tmp = []
    for c in input_data:
        if c in '<>':
            if c == '<':
                tmp.reverse()
                answer += ''.join(tmp)
                tmp = ['<']
            else:
                answer += ''.join(tmp)+'>'
                tmp = []
        elif tmp and tmp[0] != '<' and c == ' ':
            tmp.reverse()
            answer += ''.join(tmp) + ' '
            tmp = []
        else:
            tmp.append(c)
    if tmp:
        tmp.reverse()
        answer += ''.join(tmp)
    print(''.join(answer))
solv()