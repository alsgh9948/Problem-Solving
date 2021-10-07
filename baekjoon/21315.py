from sys import stdin

input = stdin.readline

n = int(input())
answer_nums = list(map(int, input().split()))

def solv():
    for k1 in range(1,n):
        if 2**k1 >= n:
            break
        tmp1 = [i for i in range(1,n+1)]
        tmp1 = mix_num(k1,tmp1,n)
        for k2 in range(1, n):
            tmp2 = [i for i in tmp1]
            if 2 ** k2 >= n:
                break
            tmp2 = mix_num(k2,tmp2,n)
            if answer_nums == tmp2:
                print(k1,k2)
                return
def mix_num(k,tmp,length):
    if k == 0:
        return tmp[::-1]
    cnt = 2**k
    tmp = mix_num(k-1,tmp[length-cnt:],cnt)+tmp[:length-cnt]
    return tmp
solv()
