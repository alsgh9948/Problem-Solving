import sys

height = None
total_height = 0

def init():
    global height, total_height
    height = [int(input()) for _ in range(9)]
    total_height = sum(height)
    height.sort()

def solv():
    for i in range(8):
        for j in range(i+1,9):
            sum = height[i] + height[j]
            if total_height - sum == 100:
                for k in range(9):
                    if k == i or k == j:
                        continue
                    print(height[k])
                return

init()
solv()