from sys import stdin,setrecursionlimit
setrecursionlimit(50001)
input = stdin.readline

tc = int(input())

def solv():
    global input_str
    input_str = input().strip()
    print(check(0,len(input_str)-1,0))
def check(left,right,flag):
    if left>=right:
        return flag
    if input_str[left] != input_str[right]:
        if flag == 1:
            return 2
        else:
            return min(check(left+1,right,1),check(left,right-1,1))
    else:
        return check(left+1, right-1, flag)
for _ in range(tc):
    solv()