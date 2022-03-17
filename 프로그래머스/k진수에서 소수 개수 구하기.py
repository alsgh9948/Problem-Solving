def solution(n, k):
    answer = 0
    str_num = convert(n,k)
    for num in str_num.split('0'):
        if not num:
            continue
        if is_prime(int(num,10)):
            answer += 1
    return answer

def is_prime(num):
    if num == 1:
        return False
    for i in range(2,int(num**(1/2))+1):
        if num%i == 0:
            return False
    return True
def convert(n,k):
    result = ''

    while n != 0:
        n,mod = divmod(n,k)
        result += str(mod)
    return result[::-1]

a = 110011
b = 10
print(solution(a,b))