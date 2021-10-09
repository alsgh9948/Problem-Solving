import sys

input = sys.stdin.readline
tc = int(input())

def solv():
    for tc_num in range(1,tc+1):
        n,k = map(int, input().split())
        num = list(input().strip())
        num_list = set()
        op = n//4
        for _ in range(op):
            for idx in range(0,n,op):
                new_num = ''
                num_list.add(int('0x'+''.join(num[idx:idx+op]),16))
            num = num[-1:]+num[:-1]
        num_list = sorted(list(num_list),reverse=True)
        print('#%d %d'%(tc_num, num_list[k-1]))
solv()