from collections import deque


def solution(begin, target, words):
    word_index = word_to_index(words)
    if begin not in word_index:
        word_index[begin] = len(word_index)

    answer = bfs(begin, target, words, word_index)
    return answer


def word_to_index(words):
    word_index = {}

    for word in words:
        word_index[word] = len(word_index)

    return word_index


def bfs(begin, target, words, word_index):
    visited = [False] * len(word_index)
    q = deque([(begin, 0)])

    start = word_index[begin]
    visited[start] = True

    while q:
        now, cnt = q.pop()
        if now == target:
            return cnt

        for word in words:
            if check_word(now, word) and not visited[word_index[word]]:
                visited[word_index[word]] = True
                q.appendleft((word, cnt + 1))
    return 0


def check_word(a, b):
    flag = False
    for idx in range(len(a)):
        if a[idx] != b[idx]:
            if flag:
                return False
            flag = True
    return True