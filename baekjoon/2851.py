nums = []
for _ in range(10):
    nums.append(int(input()))

def solv():
    answer = 9876543210
    total = 0
    for num in nums:
        total += num
        if abs(answer-100) >= abs(total-100):
            answer = total
        else:
            break
    print(answer)
solv()