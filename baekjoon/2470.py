from sys import stdin

input = stdin.readline

n = int(input())

arr = list(map(int, input().split()))

arr.sort()
def solv():
    answer_sum = 9876543210
    answer_left = 0
    answer_right = 0
    for idx in range(n-1):
        left = idx+1
        right = n-1

        while left <= right:
            mid = (left+right)//2
            tmp_sum = arr[idx]+arr[mid]
            if abs(tmp_sum) < abs(answer_sum):
                answer_sum = tmp_sum
                answer_left = idx
                answer_right = mid

            if tmp_sum > 0:
                right = mid-1
            elif tmp_sum < 0:
                left = mid+1
            else:
                print(arr[answer_left], arr[answer_right])
                return
    print(arr[answer_left],arr[answer_right])
solv()