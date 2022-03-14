from sys import stdin

input = stdin.readline

n = int(input())
input_data = input()
nums = []
ops = []
for c in input_data[1:]:
    if c.isdigit():
        nums.append(int(c))
    else:
        ops.append(c)

start = int(input_data[0])
answer = -(2^31)-1
def solv():
    insert_bracket(0,start)
    print(answer)
def insert_bracket(now,result):
    global answer
    if now == len(nums):
        answer = max(answer, result)
        return

    insert_bracket(now+1,calc(result,nums[now],ops[now]))

    if now < len(nums)-1:
        insert_bracket(now+2,calc(result,calc(nums[now],nums[now+1],ops[now+1]),ops[now]))


def calc(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b

solv()