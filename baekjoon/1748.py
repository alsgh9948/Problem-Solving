n = input()

answer = 0
op = 0
for op in range(1,len(n)):
    answer += (10**op-10**(op-1))*op
answer += ((int(n)-10**op)+1)*len(n)

print(answer)