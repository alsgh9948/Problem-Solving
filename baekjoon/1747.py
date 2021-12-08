n = int(input())

def solv():
    prime = set_prime()

    for num in prime:
        if num >= n:
            print(num)
            return
def set_prime():
    max_num = 1004000
    is_prime = [True]*(max_num)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_num**(1/2))):
        for j in range(i + i, max_num, i):
            is_prime[j] = False
    prime = [i for i in range(max_num) if is_prime[i] and is_palindrome(i)]
    return prime

def is_palindrome(num):
    num = str(num)
    for idx in range(len(num)//2):
        if num[idx] != num[len(num)-idx-1]:
            return False
    return True
solv()