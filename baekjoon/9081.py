from sys import stdin

input = stdin.readline

tc = int(input())

def solv():
    word = list(input().strip())

    next_word = next_permutation(word,len(word))
    print(''.join(next_word))

def next_permutation(target_list, n):
    i = n-1
    while(i > 0 and target_list[i-1] >= target_list[i]):
        i-=1
    if i <= 0:
        return target_list
    j = n-1
    while(target_list[i-1] >= target_list[j]):
        j-=1
    target_list[i-1], target_list[j] = target_list[j], target_list[i-1]
    j = n-1
    while i < j:
        target_list[i], target_list[j] = target_list[j], target_list[i]
        i+=1
        j-=1

    return target_list

for _ in range(tc):
    solv()