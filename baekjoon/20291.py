from sys import stdin
from collections import defaultdict
input = stdin.readline

n = int(input())
def solv():
    extensions = defaultdict(int)
    for _ in range(n):
        extension = input().strip().split('.')[1]
        extensions[extension] += 1
    answer = sorted(extensions.items())
    for row in answer:
        print(*row)
solv()