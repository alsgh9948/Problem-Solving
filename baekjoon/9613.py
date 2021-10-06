import sys

t = int(sys.stdin.readline())

def gcd_func(a,b):
    if b == 0:
        return a
    else:
       return gcd_func(b,a%b)

for _ in range(t):
    input_arr = sys.stdin.readline().split()
    n = int(input_arr[0])
    arr = list(map(int,input_arr[1:]))
    ans = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            ans += gcd_func(arr[i],arr[j])
    print(ans)