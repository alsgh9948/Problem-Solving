length = int(input())

target = [1,5,10,50]
candidate = set()
def solv():
    select_count(0,length,0)
    print(len(candidate))

def select_count(now, remain, num):
    global candidate

    if now == 3:
        candidate.add(num+target[now]*remain)
        return

    for i in range(remain+1):
        select_count(now+1, remain - i, num+target[now]*i)
solv()